from src.models.Split import Split


class PercentageSplit(Split.Split):

    def __init__(self, user, percentage):
        super().__init__(user)

        self.__percentage = None
        self.__amount = None

        self.set_percentage(percentage)

    def get_percentage(self):
        return self.__percentage

    def set_percentage(self, percentage):
        if percentage < 0:
            raise Exception("Percentage cannot be negative.")
        self.__percentage = percentage

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

