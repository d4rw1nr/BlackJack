import random

deck_values = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# GENERAL
def shuffle_deck(deck: list):
    random.shuffle(deck)

def count_cards(person: list):
    person[1] = 0
    for cards in person[0]:
        person[1] = person[1] + deck_values[cards]
    # Hands situations with As
    if ((person[1] > 21) and ('A' in person[0])): # 1 As
        person[1] = person[1] - 10
        if ((person[1] > 21) and (person[0].count("A") == 2)): # 2 A
            person[1] = person[1] - 10
            if ((person[1] > 21) and (person[0].count("A") == 3)): # 3 A
                person[1] = person[1] - 10
                if ((person[1] > 21) and (person[0].count("A") == 4)): # 4 A
                    person[1] = person[1] - 10
                    if ((person[1] > 21) and (person[0].count("A") == 4)): # 5
                        person[1] = person[1] - 10
                        if ((person[1] > 21) and (person[0].count("A") == 4)): # 6
                            person[1] = person[1] - 10
                            if ((person[1] > 21) and (person[0].count("A") == 4)): # 7
                                person[1] = person[1] - 10
                                if ((person[1] > 21) and (person[0].count("A") == 4)): # 8
                                    person[1] = person[1] - 10
                                    if ((person[1] > 21) and (person[0].count("A") == 4)): # 9
                                        person[1] = person[1] - 10
                                        if ((person[1] > 21) and (person[0].count("A") == 4)): # 10
                                            person[1] = person[1] - 10

# GAME ACTIONS
def deal(deck: list, croupier: list, player: list):
    # Croupier takes a card and counts
    croupier[0].append(deck.pop(0))
    count_cards(croupier)
    
    # Player takes a card and counts
    player[0].append(deck.pop(0))
    player[0].append(deck.pop(0))
    count_cards(player)

def winner(croupier: list, player: list):
    if (croupier[1]>21 and player[1]>21):
        result="TIE"
        return(result)
    elif (croupier[1]>21 or player[1]>21): # someone has exceeded 21 
        if (croupier[1]>21):
            result="PLAYER"
            return(result)
        elif (player[1]>21):
            result="HOUSE"
            return(result)
    elif (croupier[1]==21 and player[1]==21): # Both have 21
        if ((len(croupier[0]) == 2) and (len(player[0]) == 2)): # Both have BlackJack
            result="TIE"
            return(result)
        elif(len(croupier[0]) == 2 and (len(player[0]) != 2)): # croupier has blackjack
            result="HOUSE"
            return(result)
        elif(len(croupier[0]) != 2 and (len(player[0]) == 2)):# player has blackjack
            result="PLAYER"
            return(result)
    elif (croupier[1] == player[1]): # both have the same value
        result="TIE"
        return(result)
    elif (croupier[1] > player[1]):
        result="HOUSE"
        return(result)
    elif (croupier[1] < player[1]):
        result="PLAYER"
        return(result)


def dead_end(deck:list ,croupier: list, player: list):
    # Juega el croupier hasta que se plante
    while croupier[1] < 17:
        croupier[0].append(deck.pop(0))
        count_cards(croupier)
    # Se elige el ganador
    result = winner(croupier, player)
    return result


# PLAYER ACTIONS
def stand(deck: list, croupier: list, player: list):
    result = dead_end(deck, croupier, player)
    return result


def hit(deck: list, player: list):
    player[0].append(deck.pop(0))
    count_cards(player)


def double(deck:list, croupier: list, player:list):
    player[0].append(deck.pop(0))
    count_cards(player)
    result = dead_end(deck, croupier, player)
    return result


def split(deck:list, player: list):
    player1 = [[player[0][0]], 0, 0]
    player2 = [[player[0][1]], 0, 0]
    player1[0].append(deck.pop(0))
    player2[0].append(deck.pop(0))
    count_cards(player1)
    count_cards(player2)
    return ([player1, player2])