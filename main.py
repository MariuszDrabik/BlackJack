import os
from modules.cards import Deck
from modules.exceptions import (
    BlackJackWin,
    CroupierLoose,
    CroupierWin,
    DrawException,
    LooseError,
    PassException
    )
from modules.player import Player


class Game:
    """Main game class to manage everything
    """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.croupier = Player()
        self.games_counter = 0

    def take_player_name(self):
        """Collect player name ;-)"""
        name = input('Podaj imię: ')
        self.player = Player(name)

    def first_hand(self):
        """First hand after round start"""
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.croupier.cards = []
        self.player.cards = []
        os.system('cls||clear')
        for _ in range(1, 3):
            player_card = self.deck.pop_card()
            croupier_card = self.deck.pop_card()
            self.player.collect_card(player_card)
            self.croupier.collect_card(croupier_card)

    def game_option(self):
        """Main menu"""
        if self.games_counter == 0:
            self.games_counter += 1
            print('-'*50)
            print(f' {self.player.name} this is BlackJack GAME')
            print('-'*50)
            print('Play: 1')
            print('Exit: 0')
        else:
            self.games_counter += 1
            print('-'*50)
            print(f'{self.player.name} one more hand?: 1')
            print('Exit game: 0')

    def play_options(self):
        """Current deal menu"""
        options = {'1': 'Take card', '2': 'Pass'}
        for i, j in options.items():
            print(i, j)

    def actual_deal_stats(self):
        self.player.show_stat()
        print(f'Croupier cards {[self.croupier.cards[0]]}')
        print('-'*50)

    def show_final_stats(self):
        print()
        print('Final hand stats:')
        self.player.show_stat()
        self.croupier.show_stat()
        print()

    def player_playing(self):
        """Player decided to play and collect card or pass

        Raises:
            PassException: if player pass then croupier start play
        """
        self.first_hand()
        self.actual_deal_stats()
        while True:
            self.play_options()
            taken = input('Choose option?: ')
            if taken == '1':
                self.player.collect_card(self.deck.pop_card())
                self.actual_deal_stats()
                self.player.check_cards_value()
            elif taken == '2':
                raise PassException
            else:
                print('Not right option')

    def croupier_playing(self, player_points):
        """_summary_

        Args:
            player_points (int): take points form player to comapare

        Raises:
            CroupierWin: Croupier win
            DrawException: It's draw
            BlackJackWin: Someone have blackjach
            CroupierLoose: Croupier loose
        """
        card_value = sum([card.value for card in self.croupier.cards])

        if card_value <= 21 and card_value > player_points:
            if card_value == 21:
                raise BlackJackWin('Croupier HAVE BLACK JACK, You loose')
            raise CroupierWin('Croupier Win')

        while card_value <= 16:
            card = self.deck.pop_card()
            self.croupier.collect_card(card)
            card_value += card.value

        if card_value == player_points:
            raise DrawException('It\'s daw')

        if card_value > 21:
            if player_points == 21:
                raise BlackJackWin('Croupier Loose YOU HAVE BLACK JACK')
            raise CroupierLoose('Croupier Loose')

        if card_value == 21:
            raise BlackJackWin('Croupier HAVE BLACK JACK, You loose')

        if card_value > player_points:
            raise CroupierWin('Croupier Win')

        if card_value < player_points:
            raise CroupierLoose('Croupier Loose')

    def game(self):
        try:
            self.player_playing()
        except LooseError as error:
            self.show_final_stats()
            print(error)
        except PassException:
            try:
                print('PASS')
                player_points = sum([card.value for card in self.player.cards])
                self.croupier_playing(player_points)
                c_points = sum([card.value for card in self.croupier.cards])
                print(player_points, c_points)
            except BlackJackWin as black_jack:
                self.show_final_stats()
                print(black_jack)
            except CroupierLoose as win:
                # player_collect_coins()
                self.show_final_stats()
                print(win, 'You win!')
            except CroupierWin as loose:
                # croupier_collect_coins()
                self.show_final_stats()
                print(loose, 'You loose!')
            except DrawException as draw:
                self.show_final_stats()
                print(draw, 'No one loose!')

    def run(self):
        self.take_player_name()
        while True:
            self.game_option()
            while True:
                chosen = input('Choose option: ')
                if chosen == '1':
                    self.game()
                    break
                elif chosen == '0':
                    exit()
                else:
                    print('Not right option!')


if __name__ == '__main__':
    game = Game()
    game.run()
