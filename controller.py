import deck
import participant
import view

import copy

class BlackjackGame:
    DECK_VALUES = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    def __init__(self) -> None:
        # Modeler
        self.deck = deck.Deck()
        self.croupier = participant.Croupier()
        self.player = participant.Player()
        # View
        self.view = view.BlackjackView()

    # SET THE CONDITIONS OF THE GAME AND THE LOOP FOR ALL THE GAME
    def play(self):
        self.view.show_welcome_message()
        balance = self.view.get_balance()
        self.player.balance = balance
        input("Press Enter to start...")
        # loop for the game
        continue_playing = "y"
        while continue_playing == "y":
            self.start_game()
            self.play_game()
            self.view.show_current_balance(self.player.balance)
            continue_playing = self.view.ask_continue_playing()
            self.new_game()

    def new_game(self):
        self.player.cards = []
        self.croupier.cards = []

    def start_game(self):
        # Get the initial bet from the player
        self.current_bet = self.view.get_initial_bet(self.player.balance)
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
        pass
    
    def double(self):
        # double the bet
        self.current_bet += self.current_bet
        # play the card
        self.player.add_card(self.deck.draw_card())
        self.stand()

    # STANDARD FOR THE GAME AFTER THE FIRST HAND
    def game_standard(self):
        while self.player.values <= 21:
            action = self.view.actions_player(False, False)
            if action == "h": 
                self.hit()
            elif action == "s":
                self.stand()
                break

    # FIRST HAND OF THE GAME
    def play_game(self):
        if (self.DECK_VALUES[self.player.cards[0]] == self.DECK_VALUES[self.player.cards[1]]) and (self.player.balance >= self.current_bet*2):
            # Player choice on pairs with enough balance
            action = self.view.actions_player(True, True)
            if action == 'h': #hit
                self.hit()
                self.game_standard()
                self.finish_game()
            elif action == 's': #stand
                self.stand()
                self.finish_game()
            elif action == 'd': #double
                self.double()
                self.finish_game()
            elif action == 'sp': #split
                self.split()
        else:
            # Player choice on regular cards and validation of the amount
            if self.player.balance >= self.current_bet*2:
                action = self.view.actions_player(True, False)
            else: 
                action = self.view.actions_player(False, False)
            # Actions of the player
            if action == 'h': #hit
                self.hit()
                self.game_standard()
                self.finish_game()
            elif action == 's': #stand
                self.stand()
                self.finish_game()
            elif action == 'd': #double
                self.double()
                self.finish_game()

    def croupier_play(self):
        while self.croupier.values < 17:
            self.croupier.add_card(self.deck.draw_card())
        # Show cards
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(self.player.cards, self.player.values)

    def finish_game(self):
        self.croupier_play()
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
        # Result of the bet
        if winner == 1:
            self.player.balance += self.current_bet
        elif winner == -1:
            self.player.balance -= self.current_bet


    def split(self):
        # Double the bet on different hands
        self.current_bet_h2 = self.current_bet
        # Split of hand
        split_player = copy.deepcopy(self.player)
        del self.player.cards[-1]
        del split_player.cards[0]
        self.player.add_card(self.deck.draw_card())
        split_player.add_card(self.deck.draw_card())

        # HAND 1 PLAY
        print("-------")
        print("HAND 1")
        # Show hands
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(self.player.cards, self.player.values)
        while self.player.values <= 21:
            # Validation of the balance for double
            if self.player.balance >= ((self.current_bet*2) + self.current_bet_h2):
                action = self.view.actions_player(True, False)
            else: 
                action = self.view.actions_player(False, False)
            # Actions of the player
            if action == "h": 
                self.hit()
            elif action == "s":
                self.stand()
                break
            elif action == "d":
                self.double()
                break
        
        # HAND 2 PLAY
        print("-------")
        print("HAND 2")
        # Show hands
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(split_player.cards, split_player.values)
        # Game standard adjusted
        while split_player.values <= 21:
            # Validation for double
            if self.player.balance >= (self.current_bet + (self.current_bet_h2*2)):
                action = self.view.actions_player(True, False)
            else:
                action = self.view.actions_player(False, False)
            # ACtion of the player
            if action == "h":
                split_player.add_card(self.deck.draw_card())
                # Show cards
                self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
                self.view.show_player_hand(split_player.cards, split_player.values)
            elif action == "s":
                break
            elif action == "d":
                # double the bet
                self.current_bet_h2 += self.current_bet_h2
                # play the card
                split_player.add_card(self.deck.draw_card())
                break

        # FINISH GAME
        # Show croupier hands and player hands 
        self.croupier_play()
        self.view.show_player_hand(split_player.cards, split_player.values)
        # FINISH GAME HAND1
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
        print("--------------")
        print("HAND 1 WINNER:") # show winner on console
        self.view.show_winner(winner)
        # bet of first hand
        if winner == 1:
            self.player.balance += self.current_bet
        elif winner == -1:
            self.player.balance -= self.current_bet
        # FINISH GAME HAND2
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
        print("--------------")
        print("HAND 2 WINNER:") # show winner on console
        self.view.show_winner(winner)
        # bet of second hand
        if winner == 1:
            self.player.balance += self.current_bet_h2
        elif winner == -1:
            self.player.balance -= self.current_bet_h2