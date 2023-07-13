class Participant:

    DECK_VALUES = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    def __init__(self) -> None:
        self._cards = []
        self._values = 0

    @property
    def cards(self):
        return self._cards
    
    @property
    def values(self):
        return self._values
    
    @cards.setter
    def cards(self, new_cards):
        if isinstance(new_cards, list) and all(isinstance(card, str) for card in new_cards):
            self._cards = new_cards
            self.hand_value()
        else:
            raise ValueError("Cards must be a list of strings")

    # Essential methods
    def hand_value(self):
        self._values = 0
        for card in self._cards:
            self._values += self.DECK_VALUES[card]
        
        # Adjust for aces
        num_aces = self._cards.count("A")
        for _ in range(num_aces):
            if self._values > 21:
                self._values -= 10

    def add_card(self, card):
        self._cards.append(card)
        self.hand_value()


class Croupier(Participant):
    def __init__(self) -> None:
        super().__init__()


class Player(Participant):
    def __init__(self) -> None:
        super().__init__()
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, int):
            self._balance = new_balance
        else:
            raise ValueError("Balance must be a integer")

class Bot(Player):
    def __init__(self) -> None:
        super().__init__()

    def decide_action(self, croupier_cards, player_cards, player_value, allow_double=False, allow_split=False):
        croupier_value = self.DECK_VALUES[croupier_cards]
        # PAIRS
        if (len(player_cards) == 2) and (self.DECK_VALUES[player_cards[0]] == self.DECK_VALUES[player_cards[1]]):
            if player_cards[0] == "A":
                if allow_split:
                    return 'sp'
                else:
                    return 'h'
            elif player_cards[0] == "10":
                return 's'
            elif player_cards[0] == "9":
                if croupier_value in [7, 10, 11]:
                    return 's'
                else:
                    if allow_split:
                        return 'sp'
                    else:
                        return 'h'
            elif player_cards[0] == "8":
                if allow_split:
                    return 'sp'
                else:
                    return 'h'
            elif player_cards[0] == "7":
                if croupier_value >= 8:
                    return 'h'
                else:
                    if allow_split:
                        return 'sp'
                    else:
                        return 'h'
            elif player_cards[0] == "6":
                if croupier_value >= 7:
                    return 'h'
                else:
                    if allow_split:
                        return 'sp'
                    else:
                        return 'h'
            elif player_cards[0] == "5":
                if croupier_value >= 10:
                    return 'h'
                else:
                    if allow_double:
                        return 'd'
                    else:
                        return 'h'
            elif player_cards[0] == "4":
                if croupier_value in [5,6]:
                    if allow_split:
                        return 'sp'
                    else:
                        return 'h'
                else:
                    return 'h'
            elif player_cards[0] in ["2", "3"]:
                if croupier_value >= 8:
                    return 'h'
                else:
                    if allow_split:
                        return 'sp'
                    else:
                        return 'h'
        # Soft totals
        elif (len(player_cards) == 2) and ("A" in player_cards):
            if player_value == 21 or player_value == 20:
                return 's'
            elif player_value == 19:
                if croupier_value == 6:
                    if allow_double:
                        return 'd'
                    else:
                        return 'h'
                else:
                    return 's'
            elif player_value == 18:
                if croupier_value <= 6:
                    if allow_double:
                        return 'd'
                    else:
                        return 'h'
                elif croupier_value <= 8:
                    return 's'
                elif croupier_value >= 9:
                    return 'h'
            elif player_value == 17:
                if croupier_value in [3,4,5,6] and allow_double:
                    return 'd'
                else:
                    return 'h'
            elif player_value in [16,15]:
                if croupier_value in [4,5,6] and allow_double:
                    return 'd'
                else:
                    return 'h'
            elif player_value in [14,13]:
                if croupier_value in [5,6] and allow_double:
                    return 'd'
                else:
                    return 'h'

