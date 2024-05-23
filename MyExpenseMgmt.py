
class ExpenseManagementSystem:
    def __init__(self):
        self.expense_list = []

    def add_expense(self):
        expense_details = input("Enter expense details: ")
        amount = float(input("Enter expense amount: "))
        self.expense_list.append((expense_details, amount))
        print("Expense added successfully!")

    def delete_expense(self):
        expense_details = input("Enter expense details to delete: ")
        for expense in self.expense_list:
            if expense[0] == expense_details:
                self.expense_list.remove(expense)
                print("Expense deleted successfully!")
                return
        print("Expense not found!")

    def update_expense(self):
        expense_details = input("Enter expense details to update: ")
        for expense in self.expense_list:
            if expense[0] == expense_details:
                new_amount = float(input("Enter new expense amount: "))
                index = self.expense_list.index(expense)
                self.expense_list[index] = (expense_details, new_amount)
                print("Expense updated successfully!")
                return
        print("Expense not found!")

    def view_expenses(self):
        for expense in self.expense_list:
            print("Expense Details:", expense[0])
            print("Expense Amount:", expense[1])
            print("-----------------")

    def run(self):
        while True:
            print("1. Add Expense")
            print("2. Delete Expense")
            print("3. Update Expense")
            print("4. View Expenses")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_expense()
            elif choice == 2:
                self.delete_expense()
            elif choice == 3:
                self.update_expense()
            elif choice == 4:
                self.view_expenses()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again!")

# Example usage:
ems = ExpenseManagementSystem()
ems.run()

# Test cases:
ems.add_expense()  # Add an expense
ems.add_expense()  # Add another expense
ems.view_expenses()  # View all expenses
ems.update_expense()  # Update an expense
ems.delete_expense()  # Delete an expense
ems.view_expenses()  # View remaining expenses
