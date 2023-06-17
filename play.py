import pandas as pd

import Actions as act
import Strategies as sttgy

def play(n_games: int, bet: int):
    i = 0 # index for iteration of the number of games

    # Game activity log
    games_log = {"p_cards": [], "p_value": [], "c_cards": [], "c_value": [], "game_log":[], "winner": [], "boat": []}

    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4 # Create the deck
    act.shuffle_deck(deck) # shuffle the list deck

    while i < n_games:

        croupier = [[],0] # cards, value of the cards
        player = [[],0,[]] # cards, value of the cards, actions log

        if len(deck) < (52*0.25):
            new_deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
            deck.extend(new_deck)
            act.shuffle_deck(deck)

        act.deal(deck, croupier, player) # deal the cards 1 to croupier and 2 to player

        print("las cartas son: " , str(player[0]) , str(croupier[0]))

        result = None  # string with the text PLAYER, HOUSE or TIE for the result of the game
        while result == None:
            if ((player[0][0]==player[0][1]) and (len(player[0]) == 2)):
                result = sttgy.pairs(deck, croupier, player) # decisions if the player got the same two cards in the deal
            else:
                result = sttgy.game(deck, croupier, player) # decision if the cards in the deal are not the same
        
        if result == "PLAYER" and "D" in player[2]: bet = bet+2
        elif result == "PLAYER": bet = bet+1
        elif result == "HOUSE" and "D" in player[2]: bet = bet-2
        elif result == "HOUSE": bet = bet-1
        if len(result) == 2: # Change in the boat for a split hand game
            if result[0] == "PLAYER" and "D" in player[2]: bet = bet+2
            elif result[0] == "PLAYER": bet = bet+1
            elif result == "HOUSE" and "D" in player[2]: bet = bet-2
            elif result[0] == "HOUSE": bet = bet-1

            if result[1] == "PLAYER" and "D" in player[2]: bet = bet+2
            elif result[1] == "PLAYER": bet = bet+1
            elif result == "HOUSE" and "D" in player[2]: bet = bet-2
            elif result[1] == "HOUSE": bet = bet-1
        
        games_log["p_cards"].append(player[0])
        games_log["p_value"].append(player[1])
        games_log["c_cards"].append(croupier[0])
        games_log["c_value"].append(croupier[1])
        games_log["game_log"].append(player[2])
        games_log["winner"].append(result)
        games_log["boat"].append(bet)

        i = i+1
    
    games_df = pd.DataFrame(games_log)
    return(games_df)