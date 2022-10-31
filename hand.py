from itertools import pairwise


class Hand:

    def __init__(self, cards):
        assert len(cards) == 5
        self.cards = sorted(cards, key=lambda card: card.rank)
        self.suits = list(map(lambda card: card.suit, self.cards))
        self.ranks = list(map(lambda card: card.rank, self.cards))

    # def is_royal_flush(self):
    #     return self.is_straight_flush() and min(self.ranks) == 10

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_flush(self):
        suit_candidate = self.cards[0].suit
        return all(map(lambda suit: suit == suit_candidate, self.suits))

    def is_straight(self):
        for pair in pairwise(self.ranks):
            if pair[0] != pair[1] - 1:
                return False

        return True
