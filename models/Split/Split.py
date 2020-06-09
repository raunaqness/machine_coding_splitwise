import uuid
from models.User import User


class Split:
    """
    Split Class
    """

    id: str
    user: User
    amount: float
    type: str

    def __init__(self, user):
        self.__user = None
        self.__id = None
        self.__amount = None

        self.set_id()
        self.set_user(user)

    def __repr__(self):
        return "User : {} | Amount = {}".format(self.get_user(), self.get_amount())

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = uuid.uuid4().hex

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount
