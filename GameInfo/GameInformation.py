import random
from GameInfo.Counter import Counter
import pathlib


class GameInformation:
    DEFAULT_LIVES = 6
    WORDS_PATH = str(pathlib.Path(__file__).parent.absolute()) + r"\words.txt"

    def __init__(self):
        self.secret_word = self.generate_secret_word()
        self.letter_to_guess = list(self.secret_word)
        self.lives_counter = Counter(self.DEFAULT_LIVES)
        self.mistake_guesses = []
        self.correct_guesses = []

    def generate_secret_word(self):
        words_file = open(GameInformation.WORDS_PATH, 'r')
        words_list = words_file.read().split(",")
        words_file.close()
        secret_word = random.choice(words_list)
        return secret_word.upper()

    def input_event(self, user_input):
        user_input = user_input.upper()
        try:
            if self.check_input(user_input):
                self.correct_guesses += user_input
                self.letter_to_guess.remove(user_input)
                return True
            else:
                self.mistake_guesses += user_input
                self.lives_counter.decrease()
                return False
        except ValueError as e:
            raise e

    def check_input(self, user_input):
        if not self.is_valid_input(user_input):
            raise ValueError("Error, user input should be one new alphabetic letter!")
        else:
            return self.is_correct_guess(user_input.upper())

    def is_valid_input(self, user_input):
        return user_input.isalpha() and len(user_input) == 1 and (
            not user_input in self.mistake_guesses + self.correct_guesses)

    def is_correct_guess(self, user_input):
        return user_input.upper() in self.letter_to_guess
