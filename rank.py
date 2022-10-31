from enum import IntEnum


class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __str__(self):
        if self.value > 10:
            return self.name
        return str(self.value)
