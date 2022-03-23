import random

"""""
class Card:
    def __init__(self, value, colours):
        self.value = value
        self.colour = colour
"""""

faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

suits = ['heart', 'diamonds', 'spades', 'clubs']

suits_icon = ['♥', '♦', '♠', '♣']

## deck = [Card(value, colour) for value in range(1, 14) for colour in colours]

cards = []
for suit in suits:
    for face in faces:
        cards.append((suit, face))