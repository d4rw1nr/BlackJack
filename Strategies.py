import Actions as act

# Strategies
def hard_total(deck: list, croupier: list, player: list, stop: int):
    if player[1] >= 17:
        result=act.stand(deck, croupier, player)
        stop = stop+1
        return(result)
    elif player[1] >= 13:
        if croupier[1] >= 7:
            act.hit(deck, player)
            return(result)
        else:
            result=act.stand(deck, croupier, player)
            stop = stop+1
            return(result)
    elif player[1] == 12:
        if croupier[1] in (4,5,6):
            result=act.stand(deck, croupier, player)
            stop = stop+1
            return(result)
        else:
            act.hit(deck, player)
            return(result)
    elif player[1] == 11:
        if croupier[1] == 11:
            act.hit(deck, player)
            return(result)
        else:
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
    elif player[1] == 10:
        if croupier[1] in (10,11):
            act.hit(deck, player)
            return(result)
        else:
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
    elif player[1] == 9:
        if croupier[1] in (3,4,5,6):
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
        else:
            act.hit(deck, player)
            return(result)
    elif player[1] < 9:
        act.hit(deck, player)
        return(result)


def soft_total(deck: list, croupier: list, player: list, stop: int):
    if player[1] >= 20: # 10,9
        result=act.stand(deck, croupier, player)
        stop = stop+1
        return(result)
    elif player[1] == 19: # 8
        if croupier[1] == 6:
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
        else:
            result=act.stand(deck, croupier, player)
            stop = stop+1
            return(result)
    elif player[1] == 18: # 7
        if croupier[1] < 7:
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
        elif croupier[1] >= 9:
            act.hit(deck, player)
            return(result)
        else:
            result=act.stand(deck, croupier, player)
            stop = stop+1
            return(result)
    elif player[1] == 17: # 6
        if croupier[1] in (3,4,5,6):
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
        else:
            act.hit(deck, player)
            return(result)
    elif player[1] in (15,16): # 4 & 5
        if croupier[1] in (4,5,6):
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
        else:
            act.hit(deck, player)
            return(result)
    elif player[1] in (13,14): # 2 & 3
        if croupier[1] in (5,6):
            result=act.double(deck, croupier, player)
            stop = stop+1
            return(result)
        else:
            act.hit(deck, player)
            return(result)
