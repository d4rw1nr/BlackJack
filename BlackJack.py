from Actions import shuffle_deck
from Actions import deal
from Actions import hit

# Se crea la baraja de cartas

deck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K",]*4

def play(deck:list):
    
    values = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    shuffle_deck(deck)

    croupier = []
    player = []

    deal(deck, croupier, player)
    print("Croupier cards:" + str(croupier))
    print("Player cards:" + str(player))



play(deck)


def hard_total(deck:list,croupier:list, player:list, surrender:bool):
    values = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    if ((values[player[0]] + values[player[1]]) >= 17):
        return 