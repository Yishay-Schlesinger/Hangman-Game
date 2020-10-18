import tkinter as tk
from Frames.Frame import Frame


class InformationFrame(Frame):
    """The second frame, this frame include: lives_counter , guessed_mistakes and secret_word_state labels

        The frame's labels are updated at 'mistake_event' and 'current_event'"""

    def __init__(self, parent_frame, game_info):
        super().__init__(parent_frame)
        self.game_info = game_info
        self.secret_word_hidden = [" ", "_"] * len(self.game_info.secret_word)
        self.label_lives = None
        self.label_mistakes = None
        self.label_secret_word = None

    def initialize(self):
        self.label_lives = tk.Label(self, text=f"LIVE : {self.game_info.lives_counter}")
        self.label_mistakes = tk.Label(self, text="Mistakes: ")
        self.label_secret_word = tk.Label(self, text="Secret Word:" + "".join(self.secret_word_hidden))
        self.label_lives.pack()
        self.label_mistakes.pack()
        self.label_secret_word.pack()
        self.pack()

    def correct_event(self):
        last_correct_guess = self.game_info.correct_guesses[-1]
        letter_pos = (pos for pos, letter in enumerate(self.game_info.secret_word) if letter == last_correct_guess)
        for pos in letter_pos:
            self.secret_word_hidden[2 * pos + 1] = last_correct_guess
        self.label_secret_word["text"] = "Secret Word:" + "".join(self.secret_word_hidden)

    def mistake_event(self):
        self.label_lives["text"] = f"LIVE : {self.game_info.lives_counter}"
        last_mistake_guess = self.game_info.mistake_guesses[-1]
        self.label_mistakes["text"] += last_mistake_guess + " "

    def restart_event(self):
        super().restart_event()
        self.secret_word_hidden = [" ", "_"] * len(self.game_info.secret_word)
