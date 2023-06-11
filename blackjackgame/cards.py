#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# @uriartej


import random
from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])


class Deck:
	def __init__(self):
		self.cards = []
		ranks = [str(num) for num in range(2, 11)] + ["J", "Q", "K", "A"]
		suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

		for rank in ranks:	
			for suit in suits:
				self.cards.append(Card(rank, suit))

def shuffle(self):
	random.shuffle(self.cards)

def draw_card(self):
	return self.cards.pop(0)
