

class Card:
    def __init__(self, color, figure, value):
        self.color = color
        self.figure = figure
        self.value = value

    def __str__(self) -> str:
        return f'Card {self.figure[0]} {self.color}'

    def __repr__(self) -> str:
        return f'<Card( {self.color}, {self.figure}, {self.value})>'


class Deck:
    BLOTS = range(1, 11)
    FIGURES = ('KING', 'QUEEN', 'JACK', 'ACE')
    COLOR = ('♥', '♦', '♠', '♣')

    def __init__(self) -> None:
        self.make_black_jack_deck()
    
    def make_black_jack_deck(self):
        self.deck = [Card(j, i, i) for i in Deck.BLOTS[1:] for j in Deck.COLOR]
        for i in Deck.FIGURES:
            for j in Deck.COLOR:
                value = 10
                if i == 'ACE':
                    value = 11
                card = Card(i, j, value)
                self.deck.append(card)
        return self.deck
                
deck_1 = Deck()
print(deck_1.deck)



