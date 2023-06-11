#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# @uriartej

import pickle

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.balance = 10000
        self.wager = 0

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_hand_value(self):
        hand_value = sum(self.get_card_value(card) for card in self.hand)
        num_aces = sum(card.rank == "A" for card in self.hand)

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def get_card_value(self, card):
        if card.rank in ("J", "Q", "K"):
            return 10
        elif card.rank == "A":
            return 11
        else:
            return int(card.rank)

    def place_wager(self, amount):
        self.wager = amount
        self.balance -= amount

    def win(self):
        self.balance += self.wager * 2

    def push(self):
        self.balance += self.wager

    def __str__(self):
        return self.name


class HumanPlayer(Player):
    def save_balance(self):
        with open(f"{self.name}.pickle", "wb") as file:
            pickle.dump(self.balance, file)

    def load_balance(self):
        try:
            with open(f"{self.name}.pickle", "rb") as file:
                self.balance = pickle.load(file)
        except FileNotFoundError:
            pass


class AIPlayer(Player):
    pass
