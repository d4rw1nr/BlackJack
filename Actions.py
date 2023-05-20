import random

def shuffle_deck(deck: list):
    random.shuffle(deck)

def deal(deck: list, croupier: list, player: list):
    croupier.append(deck.pop(0))
    player.append(deck.pop(0))
    player.append(deck.pop(0))

def winner(croupier:list, player:list):
    print("gg")

def stand(deck: list, croupier: list, player: list):
    # Values of the cards in the deck
    values = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    # The croupier takes a card
    croupier.append(deck.pop(0))
    # Comparacion de 
    cr_total = 0
    for i in croupier:
        val = values[croupier[i]]
        cr_total = cr_total + val
    return("House")

def hit(deck: list, player: list):
    player.append(deck.pop(0))

def double_down(deck:list, player:list):
    player.append(deck.pop(0))

