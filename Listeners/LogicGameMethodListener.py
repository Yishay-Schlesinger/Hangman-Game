from GameInfo.GameInformation import GameInformation


class LogicGameMethodListener:
    def __init__(self, game_info):
        self.list_of_affected = []
        self.game_info = game_info

    def notify_start(self):
        for effected in self.list_of_affected:
            effected.start_event()

    def notify_mistake(self):
        for effected in self.list_of_affected:
            effected.mistake_event()
        if self.game_info.lives_counter._num == 0:
            self.notify_lose()

    def notify_correct(self):
        for effected in self.list_of_affected:
            effected.correct_event()
        if len(self.game_info.letter_to_guess) == 0:
            self.notify_win()

    def notify_win(self):
        for effected in self.list_of_affected:
            effected.win_event()

    def notify_lose(self):
        for effected in self.list_of_affected:
            effected.lose_event()

    def notify_restart(self):
        self.game_info.__init__()
        for effected in self.list_of_affected:
            effected.restart_event()
        self.notify_initialize()

    def notify_input(self, user_input):
        try:
            valid = self.game_info.input_event(user_input)
            if valid:
                self.notify_correct()
            else:
                self.notify_mistake()
        except ValueError:
            self.notify_error()

    def notify_error(self):
        for effected in self.list_of_affected:
            effected.error_event()

    def notify_initialize(self):
        for effected in self.list_of_affected:
            effected.initialize()
