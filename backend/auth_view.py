import random
import string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response

from backend.models import UserData, Team, InviteCode



# Given a user, check if the active team is invalid or NULL, and set a correct team instead
# This should be called after joining a team, leaving team, or deleting team
def validate_active_team(user):
    u_data: UserData = user.user_data

    active_team = u_data.active_team # either Team or None

     # If active_team is None, or the user is not a member of active_team...
    if active_team is None or (not user.teams.filter(id=active_team.pk).exists()):
        # ...then switch the active team to be the first team (as a default)
        u_data.active_team = user.teams.first()

        u_data.save()


def serialize_team(team: Team):
    users = [{
        "id": user.pk,
        "display_name": user.first_name,
    } for user in team.users.all()]

    return {
        "id": team.pk,
        "name": team.name,
        "users": users,
    }

# Create the AuthState object to be sent to front-end
def get_auth_state(user) -> dict:
    auth_state = {}

    if user and user.is_authenticated:
        validate_active_team(user) # replace active_team with default if it's invalid

        auth_state["is_authenticated"] = True
        auth_state["id"] = user.pk
        auth_state["email"] = user.email
        auth_state["display_name"] = user.first_name
        auth_state["teams"] = [serialize_team(team) for team in user.teams.all()]

        # active_team = UserData.objects.get(user=user).active_team
        active_team = user.user_data.active_team
        auth_state["active_team"] = active_team.pk if active_team else None

    else:
        auth_state["is_authenticated"] = False

    return auth_state


class AuthState(APIView):
    def get(self, request: HttpRequest):
        return Response(get_auth_state(request.user))


class Login(APIView):
    def post(self, request):
        credentials = request.data
        email = credentials.get("email")
        password = credentials.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)

        return Response(get_auth_state(user))


class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response(get_auth_state(None))

    def post(self, request):
        logout(request)
        return Response(get_auth_state(None))



class CreateUser(APIView):
    # I use 3 fields for users: email, password, and display_name.
    # The Django USER object has fixed fields.
    # - I store the display_name into "first_name" (last_name is unused)
    # - I store the email into both "username" and "email"
    # - Extra properties (e.g. active_team) go into UserData, which is OneToOne with User
    def post(self, request):
        credentials = request.data
        email = credentials.get("email", "")
        password = credentials.get("password", "")
        display_name = credentials.get("display_name", "")

        logout(request)

        # Request Validation
        if User.objects.filter(username=email).exists():
            # email/username already taken
            print("Username taken!")
            return Response("username-taken", status=400)

        if "" in [email, password, display_name]:
            return Response("empty-field", status=400)

        # Create User
        user = User.objects.create_user(username=email, email=email, password=password) # save User to DB
        user.first_name = display_name
        user.save() # re-save user to DB

        UserData.objects.create(user=user)

        # Sign in
        login(request, user)
        return Response(get_auth_state(user))


@method_decorator(login_required, name='dispatch')
class SetDisplayName(APIView):
    def post(self, request):
        display_name = request.data.get("display_name", "")

        user = request.user
        user.first_name = display_name # make a change
        user.save() # re-save user to DB

        auth_state_dict = get_auth_state(request.user)
        return Response(auth_state_dict)



@method_decorator(login_required, name='dispatch')
class CreateTeam(APIView):
    def post(self, request):
        payload = request.data
        team_name = payload.get("team_name")

        if team_name == "":
            return Response("empty-field", status=400)

        team = Team.objects.create(name=team_name)
        team.users.add(request.user)

        return Response(get_auth_state(request.user))


# check if user is on team
def userIsOnTeam(user: User, team: Team):
    try:
        return team.users.contains(user)
    except:
        return False

@method_decorator(login_required, name='dispatch')
class LeaveOrDeleteTeam(APIView):
    def post(self, request):
        payload = request.data
        team_id = payload.get("team_id")

        if not Team.objects.filter(id=team_id).exists():
            return Response("team-does-not-exist", 400)

        team = Team.objects.get(pk=team_id)
        user = request.user

        # Check if user is on the team:
        if not userIsOnTeam(user, team):
            return Response("not-on-team", status=403)

        # Check if team would be empty
        num_players = team.users.count()
        if (num_players == 1):
            team.delete()
        else:
            team.users.remove(user)

        return Response(get_auth_state(request.user))



@method_decorator(login_required, name='dispatch')
class CreateInviteCode(APIView):
    def generateRandomCode(self):
        length = 6
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    def post(self, request):
        payload = request.data
        team_id = payload.get("team_id")

        if not Team.objects.filter(id=team_id).exists():
            return Response("team-does-not-exist", 400)

        team = Team.objects.get(pk=team_id)
        user = request.user

        # Check if user is on the team:
        if not userIsOnTeam(user, team):
            return Response("not-on-team", status=403)

        # Generate invite code
        code = self.generateRandomCode()
        print(code)

        # Add code to database
        InviteCode.objects.create(code=code, team=team)

        return Response(code)


@method_decorator(login_required, name='dispatch')
class JoinTeamWithCode(APIView):
    def post(self, request):
        payload = request.data
        code = payload.get("invite_code")

        if not InviteCode.objects.filter(code=code).exists():
            return Response('code-does-not-exist', 400)

        inviteCode = InviteCode.objects.get(code=code)
        team = inviteCode.team
        user = request.user

        if userIsOnTeam(user, team):
            return Response('already-on-team', 400)

        team.users.add(user)
        inviteCode.delete()

        return Response(get_auth_state(user))

# ActiveTeam is the one we pull data from.
# If user wants to view data from another team, they use SetActiveTeam to select a new team.
@method_decorator(login_required, name='dispatch')
class SetActiveTeam(APIView):
    def post(self, request):
        user = request.user

        payload = request.data
        team_id = payload.get("team_id")

        if not Team.objects.filter(id=team_id).exists():
            return Response('team-does-not-exist', 400)

        active_team = Team.objects.get(id=team_id)

        user_data = UserData.objects.get(user=request.user)
        user_data.active_team = active_team
        user_data.save()

        return Response(get_auth_state(user))

