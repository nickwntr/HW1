class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message
