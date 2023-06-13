#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# @uriartej


import time
from .cards import Deck
from .player import HumanPlayer, AIPlayer

class BlackjackGame:
    def __init__(self):
        self.players = []
        self.deck = None
        self.dealer = None
        self.cut_card_position = None

    def play_game(self):
        self.setup_game()
        self.play_round()
        while self.play_again():
            self.reset_game()
            self.play_round()
        self.end_game()

    def setup_game(self):
        num_players = self.get_num_players()
        for i in range(1, num_players + 1):
            player_name = input(f"Enter player {i} name: ")
            self.players.append(HumanPlayer(player_name))

        self.players.append(AIPlayer("Dealer"))
        self.deck = Deck()

    def get_num_players(self):
        while True:
            num_players = input("Enter the number of players (1-4): ")
            if num_players.isdigit() and int(num_players) in range(1, 5):
                return int(num_players)
            else:
                print("Invalid input. Please enter a number between (1-4)")

    def play_round(self):
        for player in self.players:
            self.deal_initial_cards(player)

        for player in self.players:
            self.play_player_turn(player)

        self.play_dealer_turn()

        self.display_results()

    def deal_initial_cards(self, player):
        for _ in range(2):
            card = self.deck.draw_card()
            player.receive_card(card)

    def play_player_turn(self, player):
        print(f"\nPlayer's turn:")
        card_number = 1
        while True:
            print(player)
            choice = input("Do you want to hit? (y/n): ")
            if choice.lower() == 'y':
                card = self.deck.draw_card()
                player.receive_card(card)
                if player.get_hand_value() > 21:
                    print(f"\nCard {card_number}: {card.rank} of {card.suit}")
                    print(f"Player busted!")
                    break
                else:
                    print(f"\nCard {card_number}: {card.rank} of {card.suit}")
                    card_number += 1
            elif choice.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


    def play_dealer_turn(self):
        print("\nDealer's turn:")
        dealer = self.players[-1]
        while dealer.get_hand_value() < 17:
            card = self.deck.draw_card()
            dealer.receive_card(card)
            print(f"Dealer draws {card}")

        if dealer.get_hand_value() > 21:
            print("\nDealer busted!")

    def display_results(self):
        print("\nResults:")
        for player in self.players[:-1]:
            print(f"{player.name}: {player.get_hand_value()}")

        dealer = self.players[-1]
        dealer_value = dealer.get_hand_value()

        for player in self.players[:-1]:
            player_value = player.get_hand_value()
            if player_value > 21:
                print(f"{player.name} loses!")
            elif dealer_value > 21:
                print(f"{player.name} wins!")
            elif player_value == dealer_value:
                print(f"{player.name} pushes!")
            elif player_value > dealer_value:
                print(f"{player.name} wins!")
            else:
                print(f"{player.name} loses!")

    def play_again(self):
        while True:
            choice = input("\nDo you want to play again? (y/n): ")
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def reset_game(self):
        for player in self.players:
            player.clear_hand()
        self.deck = Deck()

    def end_game(self):
        print("Game Over")
