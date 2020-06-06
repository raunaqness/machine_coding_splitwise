import uuid


class User:
    '''
    User model
    '''

    id: int
    name: str
    email: str
    phoneNumber: str

    def __init__(self, name, email, phone_number):
        self.__id = None
        self.__name = None
        self.__email = None
        self.__phone_number = None

        self.set_id()
        self.set_name(name)
        self.set_email(email)
        self.set_phone_number(phone_number)

    def __repr__(self):
        return self.get_name()
        # return "{} {} {}".format(self.get_name(), self.get_email(), self.get_phone_number())

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id =  uuid.uuid4().hex

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number



