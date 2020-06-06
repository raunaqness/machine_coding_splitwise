from abc import ABC, abstractmethod
import uuid
from models.User import User


class Expense(ABC):
    """
    Expense class
    """

    id: int
    added_by: User
    paid_by: User
    expense_type: str
    total_amount: float
    splits: list

    def __init__(self, added_by, paid_by, expense_type, total_amount):
        self.__id = None
        self.__added_by = None
        self.__created_by = None
        self.__expense_type = None
        self.__total_amount = None
        self.__user_amounts = None
        self.__splits = []

        self.set_added_by(added_by)
        self.set_paid_by(paid_by)
        self.set_expense_type(expense_type)
        self.set_total_amount(total_amount)
        self.set_added_by(added_by)

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def update_balance(self):
        pass

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = uuid.uuid4().hex

    def get_added_by(self):
        return self.__added_by

    def set_added_by(self, added_by):
        self.__added_by = added_by

    def get_paid_by(self):
        return self.__paid_by

    def set_paid_by(self, paid_by):
        self.__paid_by = paid_by

    def get_expense_type(self):
        return self.__expense_type

    def set_expense_type(self, expense_type):
        self.__expense_type = expense_type

    def get_total_amount(self):
        return self.__total_amount

    def set_total_amount(self, total_amount):
        self.__total_amount = float(total_amount)

    def get_splits(self):
        return self.__splits

    def add_split(self, split):
        self.__splits.append(split)

    # def set_user_amounts(self, user_amounts):
    #     self.__user_amounts = user_amounts
    #
    # def get_user_amounts(self):
    #     return self.__user_amounts


