
from random import shuffle


class OptionError(Exception):
    pass


class Card:
    def __init__(self, figure: str, color: str, value: int):
        self.figure = figure
        self.color = color
        self.value = value

    def __str__(self) -> str:
        return f'Card {self.figure} {self.color}'

    def __repr__(self) -> str:
        return f'<Card({self.figure}, {self.color}, {self.value})>'

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

    def __gt__(self, other: object) -> bool:
        return self.value > other.value

    def __lt__(self, other: object) -> bool:
        return self.value < other.value


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


class Player:
    def __init__(self, name: str = 'Croupier', coins=100) -> None:
        self.name = name
        self.coins = coins
        self.cards = []

    def collect_card(self, card: Card):
        self.cards.append(card)
        return card

    def cards_value(self):
        value = sum([card.value for card in self.cards])
        return value

    def bet(self, coins):
        self.coins -= coins
        return self.coins

    def collect_coins(self, coins):
        self.coins += coins
        return self.coins


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.croupier = Player()
        self.get_player()

    def get_player(self):
        name = input('Podaj imię: ')
        self.player = Player(name)

    def first_hand(self):
        for _ in range(1, 3):
            print(_)
            card = self.deck.pop_card()
            self.player.collect_card(card)
        for _ in range(1, 3):
            print(_)
            card = self.deck.pop_card()
            self.croupier.collect_card(card)

    def check_player_cards(self):
        value = self.player.cards_value()
        if value == 22:
            return True
        return value

    def options(self):
        options = {
            '1': 'Take card',
            '2': 'Pass',
            '0': 'Exit game',
        }
        for i, j in options.items():
            print(i, j)

    def run(self):
        self.first_hand()
        print()
        print(f'{self.player.name} cards: {self.player.cards}')
        print('-'*50)
        print(f'Croupier cards {[self.croupier.cards[0]]}')
        print()
        self.options()
        while True:
            taken = input('Choose option: ')
            try:
                if taken == '0':
                    exit()
                elif taken == '1':
                    card = self.deck.pop_card()
                    self.player.collect_card(card)
                raise OptionError
            except OptionError as e:
                e = 'Not right option!'
                print(e)


if __name__ == '__main__':
    game = Game()
    game.run()
