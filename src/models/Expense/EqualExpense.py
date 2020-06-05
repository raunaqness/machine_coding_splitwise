from src.models.Expense.Expense import Expense
from src.models.Split.EqualSplit import EqualSplit

from src.Utils import utils


class EqualExpense(Expense):

    def __init__(self, added_by, paid_by, category, total_amount, users_data):
        super().__init__(added_by, paid_by, category, total_amount)

        self.__users_data = None

        self.set_users_data(users_data)


    def validate(self):
        return True

    def update_balance(self):
        users = self.get_users_data()
        no_of_users = len(users)
        for user in users:
            new_split = EqualSplit(user, (self.get_total_amount() // (no_of_users + 1)))
            self.add_split(new_split)

    def get_users_data(self):
        return self.__users_data

    def set_users_data(self, users_data):
        self.__users_data = users_data






