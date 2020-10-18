import tkinter as tk
from tkinter import font
from tkinter.font import BOLD

from Frames.Frame import Frame
from GameInfo.constant import HANGMAN_PHOTOS

class PhotosFrame(Frame):
    def __init__(self, parent_frame):
        super().__init__(parent_frame)
        self.str_var_photos = None
        self.label_photos = None
        self.hangman_photos_font = font.Font(family="Consolas", size=20, weight=BOLD)
        self.photos_generator = None

    def initialize(self):
        self.photos_generator = (photo for photo in HANGMAN_PHOTOS.values())
        self.str_var_photos = tk.StringVar()
        self.label_photos = tk.Label(self, justify=tk.LEFT, font=self.hangman_photos_font,
                                     textvariable=self.str_var_photos)
        self.label_photos.pack()

    def start_event(self):
        self._set_next_photo()
        self.pack()

    def mistake_event(self):
        self._set_next_photo()

    def _set_next_photo(self):
        try:
            next_photo = next(self.photos_generator)
            self.str_var_photos.set(next_photo)
        except:
            pass

