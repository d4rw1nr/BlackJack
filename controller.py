import deck
import participant
import view

class BlackjackGame:
    def __init__(self) -> None:
        # Modeler
        self.deck = deck.Deck()
        self.croupier = participant.Croupier()
        self.player = participant.Player()

        # View
        self.view = view.BlackjackView()
