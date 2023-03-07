from datetime import datetime
from enum import Enum
from ulticlipper.user_defned_classes.player import Player

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
        possession_type: str,
        our_score: int,
        their_score: int,
        passer: Player = None,
        receiver: Player = None,
        defender: Player = None,
        hang_time: float = None,

    ) -> None:
        self.players_on = players_on
        self.opponent=opponent
        self.tournament=tournament
        self.datetime_game=datetime_game
        self.event_type = event_type
        self.line_type = line_type
        self.possession_type = possession_type
        self.their_score = their_score
        self.our_score = our_score
        self.event_start_datetime = event_start_datetime
        self.event_start_elapsed = event_start_elapsed
        self.players_on = players_on
        self.passer = passer
        self.receiver = receiver
        self.defender = defender
        self.hang_time = hang_time

    def __str__(self) -> str:
        return f"{self.event_type}: {self.passer} {self.receiver} {self.defender}"
