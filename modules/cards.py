from random import shuffle


class Card:
    def __init__(self, figure: str, color: str, value: int):
        self.figure = figure
        self.color = color
        self.value = value

    def __str__(self) -> str:
        return f'Card {self.figure} {self.color}'

    def __repr__(self) -> str:
        return f'<Card({self.figure}, {self.color}, {self.value})>'

    def __iadd__(self, other: object) -> bool:
        return self.value + other.value


class Deck:
    BLOTS = range(2, 11)
    FIGURES = ('KING', 'QUEEN', 'JACK', 'ACE')
    COLOR = ('♥', '♦', '♠', '♣')

    def __init__(self) -> None:
        self.make_black_jack_deck()

    def __len__(self):
        return len(self.deck)

    def make_black_jack_deck(self):
        self.deck = [Card(str(i), j, i) for i in Deck.BLOTS for j in
                     Deck.COLOR]
        for i in Deck.FIGURES:
            for j in Deck.COLOR:
                value = 10
                if i == 'ACE':
                    value = 11
                card = Card(i, j, value)
                self.deck.append(card)
        return self.deck

    def shuffle_deck(self):
        shuffle(self.deck)
        return self.deck

    def pop_card(self):
        card = self.deck.pop()
        return card
