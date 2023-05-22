import Actions as act

# Se crea la baraja de cartas

deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
deck_test = ["A","K","K","6","Q","2","7","8","9","10","J","Q","K"]*4
deck_values = {"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

def play(deck:list):
    
    act.shuffle_deck(deck)

    croupier = [[],0] # cards, value of the cards
    player = [[],0,0] # cards, value of the cards, bet

    act.deal(deck, croupier, player)
    print("Croupier 1:" + str(croupier))
    print("Player 1:" + str(player))

    players = act.split(deck, player)
    print(players[0])
    print(players[1])


play(deck)


#def hard_total(deck:list,croupier:list, player:list, surrender:bool):
    #values = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    #if ((values[player[0]] + values[player[1]]) >= 17):
    #    return 