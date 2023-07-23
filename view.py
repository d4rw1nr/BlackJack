class BlackjackView:
    def print_separator(self):
        print("-------------------------------------------------------")
    
    def show_welcome_message(self):
        self.print_separator()
        print("Welcome to py_BlackJack \n by: d4rw1nr \n Good luck!")

    def get_balance(self):
        while True:
            try:
                self.print_separator()
                balance = int(input("Set your balance amount:  "))
                self.print_separator()
                return balance
            except ValueError:
                print("Please enter a number.")
    
    def add_balance(self):
        while True:
            try:
                self.print_separator()
                balance = int(input("How many more chips would you like to add to your balance:  "))
                self.print_separator()
                return balance
            except ValueError:
                print("Please enter a number.")
    
    def get_initial_bet(self, balance):
        while True:
            try:
                self.print_separator()
                bet = int(input("Enter the amount you want to bet (you have {} chips):  ".format(balance)))
                if 0 < bet <= balance:
                    return bet
                else:
                    print("Please enter a valid bet amount.")
            except ValueError:
                print("Please enter a number.")
    
    def show_current_balance(self, balance):
        self.print_separator()
        print("Your current balance is " + str(balance))

    def ask_continue_playing(self):
        self.print_separator()
        continue_playing = input("Continue playing = C \nAdd chips = A \nExit = E \n").lower()
        options = ["c", "a", "e"]
        while True:
            if continue_playing in options:
                break
            else:
                print("Invalid input, please try again.")
        return continue_playing

    def show_croupier_hand(self, cards, value):
        self.print_separator()
        print("Croupier cards: " + str(cards) + "  Value: " + str(value))

    def show_player_hand(self, cards, value):
        self.print_separator()
        print("Your cards: " + str(cards) + "  Value: " +str(value))

    # Actions avaiable for the player
    def get_action(self, options, prompt):
        while True:
            self.print_separator()
            action = input(prompt).lower()
            if action in options:
                break
            else:
                print("Invalid input, please try again.")
        return action
    
    def actions_player(self, allow_double=False, allow_split=False):
        options = ["s", "h"]
        prompt = "Choose your move: \n S = Stand   H = Hit"
        
        if allow_double:
            options.append("d")
            prompt += "   D = Double"
        if allow_split:
            options.append("sp")
            prompt += "   SP = Split"
        
        prompt += " \n"
        return self.get_action(options, prompt)
    
    def show_winner(self, winner):
        self.print_separator()
        if winner == -2:
            print("Busted")
        elif winner == -1:
            print("House Wins")
        elif winner == 0:
            print("Push")
        elif winner == 1:
            print("Player Wins")
        elif winner == 2:
            print("BlackJack!")
        else: print('ERROR!')
        self.print_separator()