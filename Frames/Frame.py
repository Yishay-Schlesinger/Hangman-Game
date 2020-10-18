import tkinter as tk


class Frame(tk.Frame):
    def initialize(self):
        pass

    def start_event(self):
        pass

    def mistake_event(self):
        pass

    def correct_event(self):
        pass

    def error_event(self):
        pass

    def win_event(self):
        pass

    def lose_event(self):
        pass

    def restart_event(self):
        for child in self.children.values():
            child.pack_forget()
