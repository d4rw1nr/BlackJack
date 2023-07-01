import random

class Deck:
    def __init__(self) -> None:
        self.cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4
        self.shuffle()

    @property
    def cards(self):
        return self.cards

    @cards.setter
    def cards(self, new_cards):
        if isinstance(new_cards, list) and all(isinstance(card, str) for card in new_cards):
            self.cards = new_cards
        else:
            raise ValueError("Cards must be a list of strings")

    def shuffle(self):
        import random
        random.shuffle(self.cards)