import deck
import participant
import view

import copy

class BlackjackGame:
    DECK_VALUES = {"A":11, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    def __init__(self, bot=False, bot_balance=100, bot_bet = 10, bot_games=10) -> None:
        # Modeler
        self.deck = deck.Deck()
        self.croupier = participant.Croupier()
        if bot:
            self.player = participant.Bot()
            self.player.balance = bot_balance
            self.bot_bet = bot_bet
            self.bot_games = bot_games
        else:
            self.player = participant.Player()
        # View
        self.view = view.BlackjackView()

    # SET THE CONDITIONS OF THE GAME AND THE LOOP FOR ALL THE GAME
    def play(self):
        if isinstance(self.player, participant.Bot): # BOT VALIDATION
            while self.bot_games != 0:
                if self.player.balance < self.bot_bet:
                    print("No more chips to play")
                    break
                else:
                    self.start_game()
                    self.play_game()
                    self.view.show_current_balance(self.player.balance)
                    self.new_game()
                    self.bot_games -= 1
        else:
            self.view.show_welcome_message()
            balance = self.view.get_balance()
            self.player.balance = balance
            input("Press Enter to start...")
            # loop for the game
            continue_playing = "y"
            while continue_playing != "e":
                if self.player.balance == 0:
                    print("You have no chips")
                    new_balance = self.view.get_balance()
                    self.player.balance = new_balance
                else:
                    self.start_game()
                    self.play_game()
                    self.view.show_current_balance(self.player.balance)
                    self.new_game()
                    continue_playing = self.view.ask_continue_playing()
                    if continue_playing == "a":
                        add_balance = self.view.add_balance()
                        self.player.balance += add_balance


    def new_game(self):
        self.player.cards = []
        self.croupier.cards = []

    def start_game(self):
        # Get the initial bet from the player
        if isinstance(self.player, participant.Bot):  # BOT VALIDATION
            self.current_bet = self.bot_bet
        else:
            self.current_bet = self.view.get_initial_bet(self.player.balance)
        # Deal de cards
        self.player.add_card(self.deck.draw_card())
        self.croupier.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        # Show cards if player is not a bot
        if isinstance(self.player, participant.Player) and not isinstance(self.player, participant.Bot): # BOT VALIDATION
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
            if isinstance(self.player, participant.Bot): # BOT VALIDATION
                action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=False, allow_split=False)
            else:
                action = self.view.actions_player(False, False)
            # decision in action based on player or bot
            if action == "h": 
                self.hit()
            elif action == "s":
                self.stand()
                break

    # FIRST HAND OF THE GAME
    def play_game(self):
        if (self.DECK_VALUES[self.player.cards[0]] == self.DECK_VALUES[self.player.cards[1]]) and (self.player.balance >= self.current_bet*2):
            # Player choice on pairs with enough balance
            if isinstance(self.player, participant.Bot): # BOT VALIDATION
                action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=True, allow_split=True)
            else:
                action = self.view.actions_player(True, True)
            # decision in action based on player or bot
            if action == 'h': #hit
                self.hit()
                self.game_standard()
                self.croupier_play()
                self.finish_game(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)
            elif action == 's': #stand
                self.stand()
                self.croupier_play()
                self.finish_game(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)
            elif action == 'd': #double
                self.double()
                self.croupier_play()
                self.finish_game(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)
            elif action == 'sp': #split
                self.split()
        else:
            # Player choice on regular cards and validation of the amount
            if self.player.balance >= self.current_bet*2:
                if isinstance(self.player, participant.Bot): # BOT VALIDATION
                    action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=True, allow_split=False)
                else:
                    action = self.view.actions_player(True, False)
            else: 
                if isinstance(self.player, participant.Bot): # BOT VALIDATION
                    action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=False, allow_split=False)
                else:
                    action = self.view.actions_player(False, False)
            # Actions of the player
            if action == 'h': #hit
                self.hit()
                self.game_standard()
                self.croupier_play()
                self.finish_game(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)
            elif action == 's': #stand
                self.stand()
                self.croupier_play()
                self.finish_game(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)
            elif action == 'd': #double
                self.double()
                self.croupier_play()
                self.finish_game(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)

    # THE CROUPIER PLAYS HIS HAND
    def croupier_play(self):
        while self.croupier.values < 17:
            self.croupier.add_card(self.deck.draw_card())
        # Show cards
        self.view.show_croupier_hand(self.croupier.cards, self.croupier.values)
        self.view.show_player_hand(self.player.cards, self.player.values)

    # RETURN WINNER -1=HOUSE_WINS 0=PUSH 1=PLAYER_WINS
    def set_winner(self, croupier_cards, croupier_values, player_cards, player_values):
        if croupier_values > 21 and player_values > 21: # both exceeded 21
            winner = -1
        elif croupier_values > 21 or player_values > 21: # someone exceeded 21
            if croupier_values > 21: # Croupier has +21
                winner = 1
            elif player_values > 21: # Player has +21
                winner = -1
        elif croupier_values == 21 and player_values == 21: # both have 21
            if len(croupier_cards) == 2 and len(player_cards) == 2: # both have blackjack
                winner = 0
            elif len(croupier_cards) == 2 and len(player_cards) != 2: # croupier has blackjack
                winner = -1
            elif len(croupier_cards) != 2 and len(player_cards) == 2: # player has blackjack
                winner = 0
        elif croupier_values == player_values: # both have same value
            winner = 0
        elif croupier_values > player_values: # croupier more than player
            winner = -1
        elif croupier_values < player_values: # croupier less than player
            winner = 1
        return winner
    
    # CONTROLS THE PAYMENTS
    def result_game(self, winner):
        # Result of the bet
        if winner == 1:
            self.player.balance += self.current_bet
        elif winner == -1:
            self.player.balance -= self.current_bet

    def finish_game(self, croupier_cards, croupier_values, player_cards, player_values):
        winner = self.set_winner(croupier_cards, croupier_values, player_cards, player_values)
        self.view.show_winner(winner)
        self.result_game(winner)

    # GAME AFTER A SPLIT
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
                if isinstance(self.player, participant.Bot): # BOT VALIDATION
                    action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=True, allow_split=False)
                else:
                    action = self.view.actions_player(True, False)
            else: 
                if isinstance(self.player, participant.Bot): # BOT VALIDATION
                    action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=False, allow_split=False)
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
                if isinstance(self.player, participant.Bot): # BOT VALIDATION
                    action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=True, allow_split=False)
                else:
                    action = self.view.actions_player(True, False)
            else:
                if isinstance(self.player, participant.Bot): # BOT VALIDATION
                    action = self.player.decide_action(self.croupier.cards, self.player.cards, self.player.values, allow_double=False, allow_split=False)
                else:
                    action = self.view.actions_player(False, False)
            # ACtion of the player/bot
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
        winner = self.set_winner(self.croupier.cards, self.croupier.values, self.player.cards, self.player.values)
        print("--------------")
        print("HAND 1 WINNER:") # show winner on console
        self.view.show_winner(winner)
        self.result_game(winner) # bet of first hand
        # FINISH GAME HAND2
        winner = self.set_winner(self.croupier.cards, self.croupier.values, split_player.cards, split_player.values)
        print("--------------")
        print("HAND 2 WINNER:") # show winner on console
        self.view.show_winner(winner)
        if winner == 1:  # bet of second hand
            self.player.balance += self.current_bet_h2
        elif winner == -1:
            self.player.balance -= self.current_bet_h2