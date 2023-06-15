#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# @uriartej


from blackjackgame.cards import Deck
from blackjackgame.player import Player


class BlackjackGame:
    def __init__(self):
        self.players = []
        self.deck = None

    def play_game(self):
        self.setup_game()
        while True:
            self.play_round()
            if not self.play_again():
                break
            self.reset_game()
        self.end_game()

    def setup_game(self):
        num_players = self.get_num_players()
        for i in range(num_players):
            player_name = input(f"Enter player {i+1} name: ")
            self.players.append(Player(player_name))
        self.deck = Deck()

    def get_num_players(self):
        while True:
            num_players = input("Enter the number of players (1-4): ")
            if num_players.isdigit() and int(num_players) in range(1, 5):
                return int(num_players)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

    def play_round(self):
        self.deck.shuffle()
        self.deal_initial_cards()
        self.display_all_hands()

        for player in self.players:
            self.play_player_turn(player)

        self.play_dealer_turn()
        self.display_all_hands()
        self.determine_results()

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                card = self.deck.draw_card()
                player.add_card(card)

    def display_all_hands(self):
        for player in self.players:
            player.display_hand()

    def play_player_turn(self, player):
        print(f"{player.name}'s turn:")
        while True:
            choice = input(f"{player.name}, do you want to hit? (yes/no): ")
            if choice.lower() == "yes":
                self.hit(player)
                self.display_all_hands()
                if self.is_bust(player):
                    print(f"{player.name} busts!")
                    break
            elif choice.lower() == "no":
                break

    def hit(self, player):
        card = self.deck.draw_card()
        player.add_card(card)

    def is_bust(self, player):
        return player.get_hand_value() > 21

    def play_dealer_turn(self):
        print("Dealer's turn:")
        dealer = Player("Dealer")
        dealer.display_hand()
        while dealer.get_hand_value() < 17:
            self.hit(dealer)
            dealer.display_hand()
            if self.is_bust(dealer):
                print("Dealer busts!")
                break

    def determine_results(self):
        dealer = Player("Dealer")
        dealer_total = dealer.get_hand_value()

        for player in self.players:
            player_total = player.get_hand_value()
            if self.is_bust(player):
                print(f"{player.name} busts!")
            elif self.is_bust(dealer):
                print(f"{player.name} wins!")
            elif player_total > dealer_total:
                print(f"{player.name} wins!")
            elif player_total < dealer_total:
                print(f"{player.name} loses!")
            else:
                print(f"{player.name} pushes!")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ")
        return choice.lower() == "yes"

    def reset_game(self):
        for player in self.players:
            player.clear_hand()
        self.deck = Deck()

    def end_game(self):
        print("Game over. Thanks for playing!")




