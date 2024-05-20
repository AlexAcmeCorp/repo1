
class Expense:
    def __init__(self, id, details, amount):
        self.id = id
        self.details = details
        self.amount = amount

expenses = []

def add_expense(id, details, amount):
    expense = Expense(id, details, amount)
    expenses.append(expense)

def delete_expense(id):
    for expense in expenses:
        if expense.id == id:
            expenses.remove(expense)
            break

def update_expense(id, new_details=None, new_amount=None):
    for expense in expenses:
        if expense.id == id:
            if new_details:
                expense.details = new_details
            if new_amount:
                expense.amount = new_amount
            break

def view_expenses():
    for expense in expenses:
        print(f'ID: {expense.id}, Details: {expense.details}, Amount: {expense.amount}')
