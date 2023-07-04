class BlackjackView:
    def print_separator(self):
        print("-------------------------------------------------------")
    
    def show_welcome_message(self):
        self.print_separator()
        print("Welcome to py_BlackJack \n by: d4rw1nr \n Good luck!")

    def show_croupier_hand(self, cards, value):
        self.print_separator()
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
        if winner == -1:
            print("House Wins")
        elif winner == 0:
            print("Draw")
        elif winner == 1:
            print("Player Wins")
        else: print('ERROR!')
        self.print_separator()