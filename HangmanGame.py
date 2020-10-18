from GameInfo.GameFlow import GameFlow


class HangmanGame:
    def __init__(self):
        self.game_flow = GameFlow()

    def generate_game(self):
        self.game_flow.initialize_game()
        self.game_flow.start_game()


if __name__ == '__main__':
    hangman_game = HangmanGame()
    hangman_game.generate_game()
