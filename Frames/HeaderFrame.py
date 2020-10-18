import tkinter as tk
from tkinter import font
from tkinter.font import BOLD

from Frames.Frame import Frame
from GameInfo.constant import HANGMAN_ASCII_ART


class HeaderFrame(Frame):
    def __init__(self, parent_frame):
        super().__init__(parent_frame)
        self.label_header = None
        self.str_var_photos = None
        self.label_photos = None
        self.header_font = font.Font(family="Consolas", size=10, weight=BOLD)

    def initialize(self):
        self.label_header = tk.Label(self, text=HANGMAN_ASCII_ART, justify=tk.LEFT, font=self.header_font)
        self.label_header.pack()
        self.pack()

    def start_event(self):
        self.pack_forget()
