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


