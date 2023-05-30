import Actions as act
import Strategies as sttgy

# Se crea la baraja de cartas

deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
deck_test = ["7","4","10","2","A","A","A","A","A","A","J","Q","K"]*4
deck_values = {"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

def play(deck:list):
    
    croupier = [[],0] # cards, value of the cards
    player = [[],0,0] # cards, value of the cards, bet

    #act.shuffle_deck(deck)

    act.deal(deck, croupier, player)
    print("Croupier 1:" + str(croupier))
    print("Player 1:" + str(player))

    result = None
    while result == None:
        if "A" in player[0]:
            result=sttgy.soft_total(deck, croupier, player)
            print("Croupier 1:" + str(croupier))
            print("Player 1:" + str(player))
        else:
            result=sttgy.hard_total(deck, croupier, player)
            print("Croupier 1:" + str(croupier))
            print("Player 1:" + str(player))
    
    return(result)



blackjack=play(deck_test)
print(blackjack)
