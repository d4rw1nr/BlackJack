import deck
import participant
import view

import copy

class BlackjackGame:
    def __init__(self) -> None:
        # Modeler
        self.deck = deck.Deck()
        self.croupier = participant.Croupier()
        self.player = participant.Player()
        # View
        self.view = view.BlackjackView()

    def start_game(self):
        self.view.show_welcome_message()
        # Deal de cards
        self.croupier.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        # Show cards
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(self.player.cards, self.player.values)
    
    # ACTIONS OF THE PLAYER
    def hit(self):
        self.player.add_card(self.deck.draw_card())
        # Show cards
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(self.player.cards, self.player.values)

    def stand(self):
        self.croupier.add_card(self.deck.draw_card())
        while self.croupier.values < 17:
            self.croupier.add_card(self.deck.draw_card())
        # Show cards
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(self.player.cards, self.player.values)
    
    def double(self):
        self.player.add_card(self.deck.draw_card())
        self.stand()


    def game_standard(self):
        while self.player.values < 21:
            action = self.view.actions_player_SH()
            if action == "h": 
                self.hit()
            elif action == "s":
                self.stand()
                break

    def play_game(self):
        if self.player.cards[0] == self.player.cards[1]:
            # Player choice on pairs
            action = self.view.actions_player_SHDP()
            if action == 'h': #hit
                self.hit()
                self.game_standard
            elif action == 's': #stand
                self.stand()
            elif action == 'd': #double
                self.double()
            elif action == 'sp': #split
                self.split()
        else:
            # Player choice on regular cards
            action = self.view.actions_player_SHD()
            if action == 'h': #hit
                self.hit()
                self.game_standard
            elif action == 's': #stand
                self.stand()
            elif action == 'd': #double
                self.double()

    def finish_game(self):
        if self.croupier.values > 21 and self.player.values > 21: # both exceeded 21
            winner = 0
        elif self.croupier.values > 21 or self.player.values > 21: # someone exceeded 21
            if self.croupier.values > 21: # Croupier has +21
                winner = 1
            elif self.player.values > 21: # Player has +21
                winner = -1
        elif self.croupier.values == 21 and self.player.values == 21: # both have 21
            if len(self.croupier.cards) == 2 and len(self.player.cards) == 2: # both have blackjack
                winner = 0
            elif len(self.croupier.cards) == 2 and len(self.player.cards) != 2: # croupier has blackjack
                winner = -1
            elif len(self.croupier.cards) != 2 and len(self.player.cards) == 2: # player has blackjack
                winner = 0
        elif self.croupier.values == self.player.values: # both have same value
            winner = 0
        elif self.croupier.values > self.player.values: # croupier more than player
            winner = -1
        elif self.croupier.values < self.player.values: # croupier less than player
            winner = 1
        # Show winner in console
        self.view.show_winner(winner)



    def split(self):
        del self.player.cards[-1]
        split_player = copy.copy(self.player)
        self.player.add_card(self.deck.draw_card())
        split_player.add_card(self.deck.draw_card())

        # HAND 1
        print("-------")
        print("HAND 1")
        print("-------")
        # Game standard adjusted
        while self.player.values < 21:
            action = self.view.actions_player_SH()
            if action == "h": 
                self.hit()
            elif action == "s":
                break
        
        # HAND 2
        print("-------")
        print("HAND 2")
        print("-------")
        # Game standard adjusted
        while split_player.values < 21:
            action = self.view.actions_player_SH()
            if action == "h":
                split_player.add_card(self.deck.draw_card())
                # Show cards
                self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
                self.view.show_player_hand(split_player.cards, split_player.values)
            elif action == "s": # Stand in second hand allow croupier to play
                self.croupier.add_card(self.deck.draw_card())
                while self.croupier.values < 17:
                    self.croupier.add_card(self.deck.draw_card())
                    break

        # Show hands
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        print("HAND 1 --------")
        self.view.show_player_hand(self.player.cards, self.player.values)
        print("HAND 2 --------")
        self.view.show_player_hand(split_player.cards, split_player.values)
        
        # Finish game - hand 1
        print("HAND 1 --------")
        self.finish_game()
        # Finish game - hand 2
        print("HAND 2 --------")
        if self.croupier.values > 21 and split_player.values > 21: # both exceeded 21
            winner = 0
        elif self.croupier.values > 21 or split_player.values > 21: # someone exceeded 21
            if self.croupier.values > 21: # Croupier has +21
                winner = 1
            elif split_player.values > 21: # Player has +21
                winner = -1
        elif self.croupier.values == 21 and split_player.values == 21: # both have 21
            if len(self.croupier.cards) == 2 and len(split_player.cards) == 2: # both have blackjack
                winner = 0
            elif len(self.croupier.cards) == 2 and len(split_player.cards) != 2: # croupier has blackjack
                winner = -1
            elif len(self.croupier.cards) != 2 and len(split_player.cards) == 2: # player has blackjack
                winner = 0
        elif self.croupier.values == split_player.values: # both have same value
            winner = 0
        elif self.croupier.values > split_player.values: # croupier more than player
            winner = -1
        elif self.croupier.values < split_player.values: # croupier less than player
            winner = 1
        # Show winner in console
        self.view.show_winner(winner)