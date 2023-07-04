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


class Player(Participant):
    def __init__(self) -> None:
        super().__init__()

class Croupier(Participant):
    def __init__(self) -> None:
        super().__init__()