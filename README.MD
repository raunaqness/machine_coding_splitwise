# Splitwise Machine Coding 

How to run : 

```
git clone https://github.com/raunaqness/machine_coding_splitwise.git
cd machine_coding_splitwise
python3 Main.py
```

**Note** - Make sure you have Python 3.6 installed on your system.

Project Structure : 

```
├── BookKeeper.py
├── Main.py
├── README.MD
├── Utils
│   ├── __init__.py
│   ├── __pycache__
│   └── utils.py
├── __init__.py
├── __pycache__
└── models
    ├── Expense
    │   ├── EqualExpense.py
    │   ├── Expense.py
    │   ├── PercentageExpense.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── Split
    │   ├── EqualSplit.py
    │   ├── PercentageSplit.py
    │   ├── Split.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── User.py
    ├── __init__.py
    └── __pycache__
```

Current list of available commands :  

```
The following function are currently available : 
        1. Add User - "add_user <name> <email> <phone_number>"
        2. View All Users - "view_all_users"
        3. View User Balance - "view_balance <name>"
        4. Add Expense :
            - Equal Expense : "add_expense <added_by> <created_by> <category> <total_amount> <expense_type> <list_of_users>"
              Eg. : "add_expense Hardeep Hardeep equal 900 Raunaq Ashish"
            - Percentage Expense : "add_expense <added_by> <created_by> <category> <total_amount> <expense_type> <list of [user, percentage]>"
              For Example : "add_expense Raunaq Raunaq percentage 500 Hardeep 25.0 Ashish 40.0"
        5. View All Expenses of a User - "view_all_expenses <name>"

```