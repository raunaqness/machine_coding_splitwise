from models.Expense import Expense
from models.Split.PercentageSplit import PercentageSplit


class PercentageExpense(Expense.Expense):
    def __init__(self, added_by, paid_by, category, total_amount, users_data):
        super().__init__(added_by, paid_by, category, total_amount)

        self.__users_data = None
        self.set_users_data(users_data)

    def validate(self):
        super().validate()

        return False

    def update_balance(self):
        users = self.get_users_data()

        for user, percentage in users:
            new_split = PercentageSplit(user, percentage)

            user_amount = self.get_total_amount() * percentage / 100
            new_split.set_amount(user_amount)

            self.add_split(new_split)

    def get_users_data(self):
        return self.__users_data

    def set_users_data(self, users_data):
        self.__users_data = users_data