from src.BookKeeper import Bookkeeper

class Main:
    def __init__(self):
        self.bookkeeper = Bookkeeper()

        print("""Welcome to Splitwise. Enter "help" to list available commands.""")

    def help(self):
        # TODO :
        pass

    def add_user(self, console_input):
        entities = console_input.split(' ')

        if len(entities) != 4:
            raise Exception("Invalid input for adding new user.")

        name, email, phone_number = entities[1:4]
        self.bookkeeper.add_user(name, email, phone_number)

    def view_all_users(self):
        self.bookkeeper.view_all_users()

    def view_balance(self, console_input):
        user_name = console_input.split(' ')[1]
        self.bookkeeper.view_balance(user_name)

    def add_expense(self, console_input):
        entities = console_input.split(' ')

        if len(entities) < 6:
            raise Exception("Invalid input for adding new expense.")

        added_by, created_by, category, total_amount, expense_type = entities[1:6]
        user_names = entities[5:]

        self.bookkeeper.add_expense(added_by, created_by, category, total_amount, user_names)

    def view_all_expenses(self):
        self.bookkeeper.view_all_expenses()


    def record_payment(self, console_input):
        pass

    def run(self):

        console_input = ""

        while console_input != "quit":
            console_input = input()

            if len(console_input) == 0:
                continue

            input_command = console_input.split(' ')[0]

            if input_command == "add_user":
                self.add_user(console_input)

            elif input_command == "view_all_users":
                self.view_all_users()

            elif input_command == "view_balance":
                self.view_balance(console_input)

            elif input_command == "record_payment":
                pass

            elif input_command == "add_expense":
                self.add_expense(console_input)

            elif input_command == "view_all_expenses":
                self.view_all_expenses()

            else:
                print("Invalid input!")


if __name__ == "__main__":
    m = Main()
    m.bookkeeper.add_user("Raunaq", "raunaq@email.com", "99999999")
    m.bookkeeper.add_user("Hardeep", "hardeep@email.com", "99889988")
    m.bookkeeper.add_user("Ashish", "ashish@email.com", "99889988")
    m.add_expense("add_expense Raunaq Raunaq percentage 500 Hardeep 25.0 Ashish 40.0")
    m.add_expense("add_expense Hardeep Hardeep equal 900 Raunaq Ashish")
    m.view_balance("view_balance Raunaq")
    m.view_balance("view_balance Hardeep")
    m.view_balance("view_balance Ashish")
    m.run()