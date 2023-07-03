import random

class Deck:
    def __init__(self) -> None:
        self._cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
        self.shuffle()

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

    def replenish_deck(self):
        if len(self._cards) < 13:
            additional_deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
            self._cards.extend(additional_deck)
            self.shuffle()

    def draw_card(self):
        return self._cards.pop()