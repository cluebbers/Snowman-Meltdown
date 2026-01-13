import game_logic

if __name__ == "__main__":
    game_logic.play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    while play_again == "y":
        game_logic.play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
