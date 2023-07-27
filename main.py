from controller import BlackjackGame

def main():
    game = BlackjackGame(bot=False, bot_balance=100, bot_bet = 10, bot_rounds=5)
    game.play()

if __name__ == "__main__":
    main()