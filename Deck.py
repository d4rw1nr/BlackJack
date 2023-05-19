import random

# Se crea la clase Deck con la baraja organizada
class Deck:

    # Metodo contructor
    def __init__(self, deck: list) -> None:
        self.deck: list = deck
    
    def __str__(self) -> str:
        deck_str = str(self.deck)
        return deck_str
    
    # Metdodos modificadores
    def set_deck(self, deck: list):
        self.deck = deck
    
    # Acciones
    def add_cards(self, newcards: list):
        self.deck.extend(newcards)
        return "Updated deck"

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return "Shuffled deck"
    
    def take_card(self) -> list:
            return(self.deck.pop(0))
        

    # Metodos consultores
    def get_card(self, index) -> str:
        return self.deck[index]
    
    def get_deck(self) -> list:
        return self.deck