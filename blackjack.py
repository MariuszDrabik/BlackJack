from random import shuffle


class Card:
    def __init__(self, color: str, figure: str, value: int):
        self._color = color
        self._figure = figure
        self._value = value

    def __str__(self) -> str:
        return f'Card {self._figure[0]} {self._color}'

    def __repr__(self) -> str:
        return f'<Card( {self._color}, {self._figure}, {self._value})>'

    def __eq__(self, other: object) -> bool:
        return self._value == other._value

    def __gt__(self, other: object) -> bool:
        return self._value > other._value

    def __lt__(self, other: object) -> bool:
        return self._value < other._value


class Deck:
    BLOTS = range(1, 11)
    FIGURES = ('KING', 'QUEEN', 'JACK', 'ACE')
    COLOR = ('♥', '♦', '♠', '♣')

    def __init__(self) -> None:
        self.make_black_jack_deck()
    
    def __len__(self):
        return len(self.deck)

    def make_black_jack_deck(self):
        self.deck = [Card(j, str(i), i) for i in Deck.BLOTS[1:] for j in
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


class Player:
    def __init__(self, name: str = 'Croupier') -> None:
        self.name = name
        self.cards = []
    
    def take_card(self, deck: Deck):
        card = deck.pop_card()
        self.cards.append(card)
        return card
    
    def pass_game():
        pass


deck_1 = Deck()
print(deck_1.deck)
print('oko'*50)

oko = deck_1.shuffle_deck()

print(oko == deck_1.deck)


print('_'*50)

print(deck_1.deck)



print(len(deck_1))



