from models.User import User
from models.Expense.EqualExpense import EqualExpense
from models.Expense.PercentageExpense import PercentageExpense
from models.Expense.ExpenseType import ExpenseType
from models.Exceptions import *


class Bookkeeper:
    """
    Singleton Pattern for Bookkeeper class
    """

    instance = None

    def __init__(self):
        if not Bookkeeper.instance:
            Bookkeeper.instance = Bookkeeper.__Bookkeeper()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    class __Bookkeeper:

        def __init__(self):
            self.users_by_name = {}  # {'name' : User}
            self.expenses = []  # {'id' : {'User' : 'expense' }}
            self.balances = {}  # {'user_id' : 'balance'}

        def view_all_users(self):
            for _, user in self.users_by_name.items():
                print(user)

        def add_user(self, name, email, phone_number):
            new_user = User(name, email, phone_number)
            self.users_by_name[new_user.get_name()] = new_user

        def view_all_expenses(self):
            for expense in self.expenses:
                u1, u2, amount = expense
                print("{} owes {} an amount of Rs. {}".format(u1, u2, amount))

        def view_balance(self, user_name):
            user = self.users_by_name.get(user_name, None)

            if user is None:
                raise UserDoesNotExist("User with Name : {} does not exist.".format(user_name))

            balance = 0
            for u1, u2, amount in self.expenses:
                if u2.get_name() == user_name:
                    balance += amount
                elif u1.get_name() == user_name:
                    balance -= amount

            if balance >= 0:
                print("{} is owed Rs. {} ".format(user_name, abs(balance)))
            else:
                print("{} owes Rs. {} ".format(user_name, abs(balance)))


        def view_user_balances(self, user_id):
            # check if user with id : user_id exists
            user = self.users_by_name.get(user_id, None)

            if user is None:
                raise UserDoesNotExist("User with ID : {} does not exist.".format(user_id))

            balance_amount = self.balances.get(user_id)
            sign = "+" if balance_amount >= 0 else "-"

            print("User {} has balance = {} {}".format(user.get_name(), sign, balance_amount))

        def add_expense(self, added_by, paid_by, expense_type_str, total_amount, users_data):

            added_by_user = self.users_by_name.get(added_by, None)
            paid_by_user = self.users_by_name.get(paid_by, None)

            if expense_type_str == "equal":
                expense_type = ExpenseType.EQUAL

                all_users = []
                for name in users_data:
                    user = self.users_by_name.get(name, None)
                    if user is None:
                        raise UserDoesNotExist("User with Name : {} does not exist.".format(name))
                    all_users.append(user)

                new_expense = EqualExpense(added_by_user, paid_by_user, expense_type, total_amount, all_users)

            elif expense_type_str == "percentage":
                expense_type = ExpenseType.PERCENTAGE

                all_users = []
                for i in range(len(users_data)//2):
                    name, percentage = users_data[(2*i)], users_data[(2*i)+1]
                    user = self.users_by_name.get(name, None)
                    if user is None:
                        raise UserDoesNotExist("User with Name : {} does not exist.".format(name))
                    all_users.append([user, float(percentage)])

                new_expense = PercentageExpense(added_by_user, paid_by_user, expense_type, total_amount, all_users)

            else:
                raise InvalidExpenseType("Invalid Expense type")

            new_expense.validate()
            new_expense.update_balance()

            paid_by_user = new_expense.get_paid_by()
            for split in new_expense.get_splits():
                user, split_amount = split.get_user(), split.get_amount()
                self.expenses.append([user, paid_by_user, split_amount])

            self.view_all_expenses()

        def record_settlement(self, user1, user2):
            pass
            # TODO

