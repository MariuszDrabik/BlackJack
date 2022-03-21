from modules.cards import Card, Deck
from modules.player import Player

COLOR = ('♥', '♦', '♠', '♣')


def test_card():
    king = Card('♥', 'KING', 10)
    ten = Card('♥', '8', 8)

    assert king.value == 10
    assert ten.value == 8


def test_deck():
    deck = Deck()

    assert len(deck) == 52


def test_player():
    diler = Player()
    user = Player('User')

    assert diler.name == 'Croupier'
    assert user.name == 'User'
