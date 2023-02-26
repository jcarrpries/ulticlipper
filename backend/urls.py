from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from backend.sync_view import SyncUpload, SyncChooseGame, SyncCommit
from backend.auth_view import (
    CreateUser,
    AuthState,
    SetDisplayName,
    Login,
    Logout,
    CreateTeam,
    LeaveOrDeleteTeam,
    CreateInviteCode,
    JoinTeamWithCode,
    SetActiveTeam
)

urlpatterns = [
    path('sync/upload/', SyncUpload.as_view()),
    path('sync/choosegame/', SyncChooseGame.as_view()),
    path('sync/commit/', SyncCommit.as_view()),

    path('clips/', views.ClipList.as_view()),
    path('clips/<int:pk>/', views.ClipDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>/', views.TagDetail.as_view()),
	path('tag_groups/', views.TagGroupList.as_view()),
    path('tag_groups/<int:pk>/', views.TagGroupDetail.as_view()),
	path('videos/', views.VideoList.as_view()),

    path('clips_by_video/<int:pk>/', views.ClipsByVideo.as_view()),

    path('healthcheck/', views.HealthCheck.as_view()),
    path('cleardatabase/', views.ClearDatabase.as_view()),

    path('createuser/', CreateUser.as_view()),
    path('authstate/', AuthState.as_view()),
    path('setdisplayname/', SetDisplayName.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),

    path('create_team/', CreateTeam.as_view()),
    path('leave_or_delete_team/', LeaveOrDeleteTeam.as_view()),
    path('create_invite_code/', CreateInviteCode.as_view()),
    path('join_team_with_code/', JoinTeamWithCode.as_view()),
    path('set_active_team/', SetActiveTeam.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
