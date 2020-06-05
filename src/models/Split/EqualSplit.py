
from src.models.Split import Split


class EqualSplit(Split.Split):

    def __init__(self, user, amount):
        super().__init__(user)
        self.set_amount(amount)
