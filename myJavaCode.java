
import java.util.*;

class Expense {
    String detail;
    double amount;

    Expense(String detail, double amount) {
        this.detail = detail;
        this.amount = amount;
    }
}

class ExpenseManager {
    List<Expense> expenses = new ArrayList<>();

    void addExpense(String detail, double amount) {
        expenses.add(new Expense(detail, amount));
    }

    void deleteExpense(int index) {
        expenses.remove(index);
    }

    void updateExpense(int index, String detail, double amount) {
        expenses.set(index, new Expense(detail, amount));
    }

    void viewExpenses() {
        for (Expense expense : expenses) {
            System.out.println("Detail: " + expense.detail + ", Amount: " + expense.amount);
        }
    }
    
public static void main(String[] args) {
    ExpenseManager manager = new ExpenseManager();

    // Add expenses
    manager.addExpense("Groceries", 50.0);
    manager.addExpense("Rent", 500.0);
    manager.addExpense("Utilities", 100.0);

    // View expenses
    manager.viewExpenses();

    // Update an expense
    manager.updateExpense(0, "Groceries", 60.0);

    // Delete an expense
    manager.deleteExpense(1);

    // View expenses after update and delete
    manager.viewExpenses();
}
}
