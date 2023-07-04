from controller import BlackjackGame

def main():
    game = BlackjackGame()
    
    game.start_game()
    
    game.play_game()
    
    game.finish_game()

if __name__ == "__main__":
    main()