from itertools import product
from random import shuffle

from card import Card
from rank import Rank
from suit import Suit


class Deck:

    def __init__(self):
        self.cards = [Card(suit, rank) for suit, rank in product(Suit, Rank)]
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)
