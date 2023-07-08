import random

class Deck:
    def __init__(self) -> None:
        self.total_decks = 6 # Total of decks to play, its usual to face more than a unique deck in casinos
        self._cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4*self.total_decks
        self.shuffle()
        self.replenish_threshold = len(self._cards) // 2

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards):
        if isinstance(new_cards, list) and all(isinstance(card, str) for card in new_cards):
            self._cards = new_cards
        else:
            raise ValueError("Cards must be a list of strings")

    def shuffle(self):
        random.shuffle(self._cards)

    def replenish_deck(self): # Change of the deck if the number of cards is lower than the half of the initial cards
            self._cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4*self.total_decks
            self.shuffle()

    def draw_card(self): # Change of the deck if the number of cards is lower than the half of the initial cards
        if len(self._cards) < self.replenish_threshold:
            self.replenish_deck()
        return self._cards.pop()