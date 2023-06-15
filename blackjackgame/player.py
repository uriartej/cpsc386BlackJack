#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# @uriartej

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        total = 0
        num_aces = 0

        for card in self.hand:
            if card.rank.isdigit():
                total += int(card.rank)
            elif card.rank in ["J", "Q", "K"]:
                total += 10
            elif card.rank == "A":
                num_aces += 1

        total += num_aces  # Count Aces as 1 initially

        # Adjust for Aces as 11 if it doesn't bust the hand
        while num_aces > 0 and total <= 11:
            total += 10
            num_aces -= 1

        return total

    def display_hand(self):
        print(f"{self.name}'s hand: ", end="")
        for card in self.hand:
            print(f"[{card.rank} of {card.suit}]", end=" ")
        print()

    def clear_hand(self):
        self.hand = []