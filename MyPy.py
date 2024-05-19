expenses = []

def add_expense(expense_detail, expense_amount):
    expense = {'detail': expense_detail, 'amount': expense_amount}
    expenses.append(expense)

def delete_expense(expense_id):
    if expense_id < len(expenses):
        del expenses[expense_id]

def update_expense(expense_id, new_detail, new_amount):
    if expense_id < len(expenses):
        expenses[expense_id] = {'detail': new_detail, 'amount': new_amount}

def view_expenses():
    for expense in expenses:
        print(expense)
