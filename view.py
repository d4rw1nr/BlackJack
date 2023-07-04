class BlackjackView:
    def show_welcome_message(self):
        print("-------------------------------------------------------")
        print("Welcome to py_BlackJack \n by: d4rw1nr \n Good luck!")
        print("-------------------------------------------------------")

    def show_croupier_hand(self, cards, value):
        print("-------------------------------------------------------")
        print("Croupier cards: " + str(cards) + "  Value: " + str(value))
        print("-------------------------------------------------------")

    def show_player_hand(self, cards, value):
        print("-------------------------------------------------------")
        print("Your cards: " + str(cards) + "  Value: " +str(value))
        print("-------------------------------------------------------")

    # Actions aviable for the player
    def actions_player_SH(self):
        while True:
            action = input("Choose your move: \n S = Stand   H = Hit \n").lower()
            if action in ["s","h"]:
                break
            else: print("Invalid input, please try again.")
        return action

    def actions_player_SHD(self):
        while True:
            action = input("Choose your move: \n S = Stand   H = Hit   D = Double \n").lower()
            if action in ["s","h","d"]:
                break
            else: print("Invalid input, please try again.")
        return action
    
    def actions_player_SHP(self):
        while True:
            action = input("Choose your move: \n S = Stand   H = Hit   SP = Split \n").lower()
            if action in ["s","h","sp"]:
                break
            else: print("Invalid input, please try again.")
        return action
    
    def actions_player_SHDP(self):
        while True:
            action = input("Choose your move: \n S = Stand   H = Hit   D = Double   SP = Split \n").lower()
            if action in ["s","h","d","sp"]:
                break
            else: print("Invalid input, please try again.")
        return action
    
    def show_winner(self, winner):
        if winner == -1:
            print('------------')
            print("House Wins")
            print('------------')
        elif winner == 0:
            print('------------')
            print("Draw")
            print('------------')
        elif winner == 1:
            print('------------')
            print("Player Wins")
            print('------------')
        else: print('ERROR!')