from enum import Enum
from datetime import datetime

class Gender(Enum):
    MAN_MATCHING = 1
    WOMAN_MATCHING = 2


class Position(Enum):
    HANDLER = 1
    CUTTER = 2
    HYBRID = 3


class Player:
    def __init__(
        self,
        nickname: str,
        team: str = None,
        number: int = None,
        gender: Gender = None,
        position: Position = None,
        name: str = None,
    ) -> None:
        self.name = name
        self.number = number
        self.gender = gender
        self.position = position
        self.team = team
        self.nickname = nickname

    def __str__(self) -> str:
        return f"{self.nickname}"

    def __hash__(self):
        return hash(
            (
                self.name,
                self.number,
                self.gender,
                self.position,
                self.team,
                self.nickname,
            )
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.nickname == other.nickname
            and self.team == other.team
        )


class LineType(Enum):
    O = 1
    D = 2


class EventType(Enum):
    PULL = 1
    # pull that lands out of bounds
    PULLOB = 2
    GOAL = 3
    THROWAWAY = 4
    CATCH = 5
    DROP = 6
    D = 7
    # getting a callahan (D and Goal)
    CALLAHAN = 8
    STALL = 9
    PENALIZED = 10
    # throwing a callahan
    CALLAHAND = 11,
    ENDOFFIRSTQUARTER = 12, 
    HALFTIME = 13, 
    ENDOFTHIRDQUARTER = 14,
    GAMEOVER = 15,
    ENDOFFOURTHQUARTER = 16,
    ENDOFOVERTIME = 17,


class Event:
    def __init__(
        self,
        event_type: EventType,
        opponent: str, 
        tournament: str,
        datetime_game: datetime,
        event_start_datetime: datetime,
        event_start_elapsed: int,
        players_on: list[Player],
        line_type: LineType,
        our_score: int,
        their_score: int,
        passer: Player = None,
        reciever: Player = None,
        defender: Player = None,
        hang_time: float = None,

    ) -> None:
        self.players_on = players_on
        self.opponent=opponent
        self.tournament=tournament
        self.datetime_game=datetime_game
        self.event_type = event_type
        self.line_type = line_type
        self.their_score = their_score
        self.our_score = our_score
        self.event_start_datetime = event_start_datetime
        self.event_start_elapsed = event_start_elapsed
        self.players_on = players_on
        self.passer = passer
        self.reciever = reciever
        self.defender = defender
        self.hang_time = hang_time

    def __str__(self) -> str:
        return f"{self.event_type}: {self.passer} {self.reciever} {self.defender}"

    def serialize(self):
        ret = vars(self)
        ret['players_on'] = [player.nickname for player in self.players_on]
        ret['event_type'] = str(self.event_type.name)
        ret['line_type'] = str(self.line_type.name)
        del ret['event_start_datetime']
        return ret


class Game:
    def __init__(
        self,
        opponent: str, 
        tournament: str,
        active_players: list[Player],
        datetime_of_first_pull: datetime,
        elapsed_time_of_first_pull: int, 
        starting_line_type: LineType,
        our_final_score: int, 
        their_final_score: int, 
        duration_s: int,
        events:list[Event]
    ) -> None:
        self.opponent=opponent
        self.tournament=tournament
        self.active_players=active_players
        self.time_of_first_pull=datetime_of_first_pull
        self.elapsed_time_of_first_pull= elapsed_time_of_first_pull
        self.starting_line_type=starting_line_type
        self.our_final_score=our_final_score 
        self.their_final_score= their_final_score
        self.duration_s=duration_s
        self.events=events
    
    def __str__(self) -> str:
        return f"{self.event_type}: {self.passer} {self.reciever} {self.defender}"
