import Actions as act
import Strategies as sttgy

# Se crea la baraja de cartas

deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
deck_test = ["6","7","7","A","5","3","10","J","5","9","J","Q","K"]*4
deck_values = {"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

def play(deck:list):
    
    croupier = [[],0] # cards, value of the cards
    player = [[],0,0] # cards, value of the cards, bet

    act.shuffle_deck(deck)

    act.deal(deck, croupier, player)
    print("Croupier 0:" + str(croupier))
    print("Player 0:" + str(player))

    result = None
    while result == None:
        if ((player[0][0]==player[0][1]) and (len(player[0]) == 2)):
            result = sttgy.pairs(deck, croupier, player)
        else:
            result = sttgy.game(deck, croupier, player)
    
    return(result)



blackjack=play(deck)
print(blackjack)
