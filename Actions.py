import random

def shuffle_deck(deck: list):
    random.shuffle(deck)

def deal(deck: list, croupier: list, player: list):
    croupier.append(deck.pop(0))
    player.append(deck.pop(0))
    player.append(deck.pop(0))

def hit(deck: list, player: list):
    player.append(deck.pop(0))

