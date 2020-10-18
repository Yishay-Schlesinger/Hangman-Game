import tkinter as tk
from Frames.Frame import Frame
from GameInfo.constant import DEFAULT_PADX, DEFAULT_PADY


class InputFrame(Frame):
    def __init__(self, parent_frame, listener):
        super().__init__(parent_frame)
        self.listener = listener
        self.label_command = None
        self.entry_input = None
        self.button_guess = None
        self.user_input = tk.StringVar()

    def initialize(self):
        self.user_input.set("")
        self.label_command = tk.Label(self, text="Guess a letter:", justify=tk.LEFT)
        self.entry_input = tk.Entry(self, justify=tk.LEFT, width=10, state=tk.DISABLED)
        self.button_guess = tk.Button(self, text="Guess", justify=tk.LEFT,
                                      command=lambda: self._notify_input(), state=tk.DISABLED)
        self.label_command.pack(side=tk.LEFT)
        self.entry_input.pack(side=tk.LEFT, padx=DEFAULT_PADX)
        self.button_guess.pack(side=tk.LEFT)
        self.pack(pady=DEFAULT_PADY)

    def start_event(self):
        self.button_guess["state"] = tk.NORMAL
        self.entry_input["textvariable"] = self.user_input
        self.entry_input["state"] = tk.NORMAL
        self.entry_input.bind("<Return>", self._notify_input)

    def _notify_input(self, event=None):
        input_str = self.user_input.get()
        self.user_input.set("")
        self.listener.notify_input(input_str)

    def win_event(self):
        self.end_event()

    def lose_event(self):
        self.end_event()

    def end_event(self):
        self.button_guess["state"] = tk.DISABLED
        self.entry_input["state"] = tk.DISABLED
        self.entry_input.unbind("<Return>")
