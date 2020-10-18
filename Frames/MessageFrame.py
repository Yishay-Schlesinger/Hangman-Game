from Frames.Frame import Frame
from tkinter import messagebox


class MessageFrame(Frame):
    def __init__(self, parent_frame, secret_word):
        super().__init__(parent_frame)
        self.secret_word = secret_word

    def error_event(self):
        messagebox.showinfo("Error", "Please guess ONE NEW ALPHABETIC letter!")

    def win_event(self):
        messagebox.showinfo("Winner", "YOU WIN!")

    def lose_event(self):
        messagebox.showinfo(":(", "YOU LOST, THE WORD IS: " + self.secret_word)
