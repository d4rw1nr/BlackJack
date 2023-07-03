class Participant:
    def __init__(self) -> None:
        self._cards = []
        self.values = 0

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, new_cards):
        if isinstance(new_cards, list) and all(isinstance(card, str) for card in new_cards):
            self._cards = new_cards
            self.hand_value()
        else:
            raise ValueError("Cards must be a list of strings")

    # Essential methods
    def hand_value(self):
        self.values = 0
        deck_values = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        for card in self._cards:
            self.values += deck_values[card]
        
        # Adjust for aces
        num_aces = self._cards.count("A")
        for _ in range(num_aces):
            if self.values > 21:
                self.values -= 10

    def add_card(self, card):
        self._cards.append(card)
        self.hand_value()


class Player(Participant):
    def __init__(self) -> None:
        super().__init__()

class Croupier(Participant):
    def __init__(self) -> None:
        super().__init__()