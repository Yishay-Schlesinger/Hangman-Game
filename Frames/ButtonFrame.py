import tkinter as tk

from Frames.Frame import Frame
from GameInfo.constant import DEFAULT_PADY, DEFAULT_PADX


class ButtonFrame(Frame):
    """The top frame. This frame include start, restart and exit buttons.

    At the beginning restart_button is unpack.
    After 'start_event()' start_button is unpack and restart_button is pack"""

    def __init__(self, parent_frame, listener):
        super().__init__(parent_frame)
        self.listener = listener
        self.start_button = None
        self.restart_button = None
        self.exit_button = None

    def initialize(self):
        self.start_button = tk.Button(self, command=self.listener.notify_start, padx=DEFAULT_PADX, text="START GAME")
        self.restart_button = tk.Button(self, command=self.listener.notify_restart, padx=DEFAULT_PADX, text="Restart")
        self.exit_button = tk.Button(self, command=exit, padx=DEFAULT_PADX, text="Exit")
        # pack the button to the frame. At the beginning restart_button is unpack
        self.start_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)
        self.pack(pady=DEFAULT_PADY)

    def start_event(self):
        """Unpack start_button and pack restart_button"""
        self.start_button.pack_forget()
        self.restart_button.pack(side=tk.LEFT)
