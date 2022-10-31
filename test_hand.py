from itertools import product

from card import Card
from hand import Hand
from rank import Rank
from suit import Suit


def test_is_flush_happy_path():
    cards = [Card(Suit.Club, rank) for rank in list(Rank)[:5]]
    assert Hand(cards).is_flush()


def test_is_flush_negative():
    cards = [Card(Suit.Club, Rank.TWO), Card(Suit.Heart, Rank.TWO), Card(Suit.Heart, Rank.THREE),
             Card(Suit.Heart, Rank.FOUR), Card(Suit.Heart, Rank.FIVE)]
    assert not Hand(cards).is_flush()


def test_is_straight_happy_path():
    cards = [Card(Suit.Club, Rank.TEN), Card(Suit.Club, Rank.Jack), Card(Suit.Club, Rank.Queen),
             Card(Suit.Club, Rank.King), Card(Suit.Club, Rank.Ace)]
    assert Hand(cards).is_straight()


def test_is_straight_not_sorted():
    cards = [Card(Suit.Club, Rank.TEN), Card(Suit.Club, Rank.Jack), Card(Suit.Club, Rank.King),
             Card(Suit.Club, Rank.Queen), Card(Suit.Club, Rank.Ace)]
    assert Hand(cards).is_straight()


def test_is_straight_negative():
    cards = [Card(Suit.Club, Rank.TWO), Card(Suit.Club, Rank.FOUR), Card(Suit.Club, Rank.FIVE),
             Card(Suit.Club, Rank.SIX), Card(Suit.Club, Rank.SEVEN)]
    assert not Hand(cards).is_straight()


def test_is_straight_flush_happy_path():
    cards = [Card(Suit.Club, Rank.TEN), Card(Suit.Club, Rank.Jack), Card(Suit.Club, Rank.Queen),
             Card(Suit.Club, Rank.King), Card(Suit.Club, Rank.Ace)]
    assert Hand(cards).is_straight_flush()


def test_is_straight_flush_wrong_rank():
    cards = [Card(Suit.Club, Rank.TWO), Card(Suit.Club, Rank.Jack), Card(Suit.Club, Rank.Queen),
             Card(Suit.Club, Rank.King), Card(Suit.Club, Rank.Ace)]
    assert not Hand(cards).is_straight_flush()


def test_is_straight_flush_wrong_suit():
    cards = [Card(Suit.Heart, Rank.TEN), Card(Suit.Club, Rank.Jack), Card(Suit.Club, Rank.Queen),
             Card(Suit.Club, Rank.King), Card(Suit.Club, Rank.Ace)]
    assert not Hand(cards).is_straight_flush()
