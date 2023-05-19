from Deck import Deck

# Se crea la baraja de cartas
suits = ["♥","♦","♣","♠"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K",]
cards = []

for suit in suits:
    for value in values:
        cards.append(value+suit)

deck:Deck = Deck(cards)

def BlackJack(deck: Deck, bet: float):
    
    deck.shuffle_deck()

    print("deck before game:" + str(deck))

    croupier = []
    player = []

    if deck:
        croupier.append(deck.take_card())
        player.append(deck.take_card())
        player.append(deck.take_card())

    print(croupier)
    print(player)
    print("deck after game:" + str(deck))

BlackJack(deck, 2)