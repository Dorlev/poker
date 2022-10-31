from rank import Rank
from suit import Suit


class Card:

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return str((self.suit.name, str(self.rank)))
