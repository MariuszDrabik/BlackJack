from modules.cards import Card
from modules.exceptions import BlackJackWin, LooseError


class Player:
    def __init__(self, name: str = 'Croupier', coins=100) -> None:
        self.name = name
        self.coins = coins
        self.cards = []

    def collect_card(self, card: Card):
        self.cards.append(card)
        return card
    
    def show_stat(self):
        """Player cards value"""
        print('-'*50)
        print(f'{self.name} cards: {self.cards}')
        print(f'Points: {sum(card.value for card in self.cards)}')
        print('-'*50)

    def check_cards_value(self):
        value = sum([card.value for card in self.cards])
        aces = [card.figure for card in self.cards if card.figure == 'ACE']
        if value == 21:
            return 21
        if value == 22 and len(self.cards) == 2:
            return 21
        if value > 21:
            value -= 10
            if value > 21 and aces:
                value -= 10
                if value > 21:
                    raise LooseError('Sorry You are Lossing')
                return value
            raise LooseError('Sorry You are Lossing')
        if value < 21:
            return value

    def bet(self, coins):
        self.coins -= coins
        return self.coins

    def collect_coins(self, coins):
        self.coins += coins
        return self.coins
