from blackjack import Card, Deck

COLOR = ('♥', '♦', '♠', '♣')


def test_card():
    king = Card('♥', 'KING', 10)
    ten = Card('♥', '8', 8)
    
    assert king != ten
    assert king > ten
    assert ten < king


def test_deck():
    deck = Deck()
    
    assert len(deck) == 52
    