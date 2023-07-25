from controller import BlackjackGame

def main():
    game = BlackjackGame(bot=True, bot_balance=100, bot_bet = 10, bot_rounds=5)
    game.play()

if __name__ == "__main__":
    main()