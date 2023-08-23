from controller import BlackjackGame

def main():
    games = 1000
    while games != 0:
        game = BlackjackGame(bot=True, bot_balance=100, bot_bet = 10, bot_rounds=500)
        game.play()
        games -= 1

if __name__ == "__main__":
    main()