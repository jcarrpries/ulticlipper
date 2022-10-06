from enum import Enum


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
