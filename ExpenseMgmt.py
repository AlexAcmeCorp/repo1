class ExpenseManagement:
    def __init__(self):
        self.expenses = []

    def add_expense(self, id, details, amount):
        self.expenses.append({'id': id, 'details': details, 'amount': amount})

    def delete_expense(self, id):
        self.expenses = [expense for expense in self.expenses if expense['id'] != id]

    def update_expense(self, id, new_details, new_amount):
        for expense in self.expenses:
            if expense['id'] == id:
                expense['details'] = new_details
                expense['amount'] = new_amount

    def view_expenses(self):
        for expense in self.expenses:
            print(f"ID: {expense['id']}, Details: {expense['details']}, Amount: {expense['amount']}")
