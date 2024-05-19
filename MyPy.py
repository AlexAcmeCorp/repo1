
expenses = []

def add_expense(details, amount):
    expense = {'details': details, 'amount': amount}
    expenses.append(expense)

def delete_expense(identifier):
    for expense in expenses:
        if expense['details'] == identifier:
            expenses.remove(expense)

def update_expense(identifier, new_details, new_amount):
    for expense in expenses:
        if expense['details'] == identifier:
            expense['details'] = new_details
            expense['amount'] = new_amount

def view_expenses():
    for expense in expenses:
        print(expense)


nnnnnnnnn
