class Counter:
    def __init__(self, num):
        self._num = num

    def increase(self, add=1):
        self._num += add

    def decrease(self, decrease=1):
        self._num -= decrease

    def __str__(self):
        return str(self._num)