from datetime import datetime

from ulticlipper.user_defned_classes.event import LineType, Event
from ulticlipper.user_defned_classes.player import Player


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
