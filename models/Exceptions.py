

class UserDoesNotExist(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class InvalidExpenseType(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class InvalidInput(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class SettleUpException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)
