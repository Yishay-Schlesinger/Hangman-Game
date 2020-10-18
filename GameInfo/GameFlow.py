import tkinter as tk

from Frames.ButtonFrame import ButtonFrame
from Frames.HeaderFrame import HeaderFrame
from Frames.InformationFrame import InformationFrame
from Frames.InputFrame import InputFrame
from Frames.MessageFrame import MessageFrame
from Frames.PhotosFrame import PhotosFrame
from GameInfo.GameInformation import GameInformation
from Listeners.LogicGameMethodListener import LogicGameMethodListener


class GameFlow:
    MAIN_WINDOW_SIZE = '350x380'
    MAIN_WINDOW_TITLE = "HANGMAN GAME"

    def __init__(self):
        self.game_info = GameInformation()
        self.listener = LogicGameMethodListener(self.game_info)
        self.main_window = tk.Tk()

    def initialize_game(self):
        self.main_window.geometry(GameFlow.MAIN_WINDOW_SIZE)
        self.main_window.title(GameFlow.MAIN_WINDOW_TITLE)
        self.main_window.resizable(0, 0)
        frame1 = ButtonFrame(self.main_window, self.listener)
        frame2 = InformationFrame(self.main_window, self.game_info)
        frame3 = InputFrame(self.main_window, self.listener)
        frame4 = HeaderFrame(self.main_window)
        frame5 = PhotosFrame(self.main_window)
        frame6 = MessageFrame(self.main_window, self.game_info.secret_word)
        self.listener.list_of_affected = list(self.main_window.children.values())

    def start_game(self):
        self.listener.notify_initialize()
        self.main_window.mainloop()
