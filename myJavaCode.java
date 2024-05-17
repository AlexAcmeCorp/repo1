
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ExpenseManager {
    private ArrayList<Map<String, Object>> expenses = new ArrayList<>();

    public void addExpense(String details, double amount) {
        Map<String, Object> expense = new HashMap<>();
        expense.put("details", details);
        expense.put("amount", amount);
        expenses.add(expense);
    }

    public void deleteExpense(String identifier) {
        expenses.removeIf(expense -> expense.get("details").equals(identifier));
    }

    public void updateExpense(String identifier, String newDetails, double newAmount) {
        for (Map<String, Object> expense : expenses) {
            if (expense.get("details").equals(identifier)) {
                expense.put("details", newDetails);
                expense.put("amount", newAmount);
            }
        }
    }

    public void viewExpenses() {
        for (Map<String, Object> expense : expenses) {
            System.out.println(expense);
        }
    }

    public static void main(String[] args) {
        ExpenseManager manager = new ExpenseManager();
        manager.addExpense("Groceries", 50);
        manager.addExpense("Rent", 500);
        manager.viewExpenses();
        manager.updateExpense("Groceries", "Groceries for June", 60);
        manager.viewExpenses();
        manager.deleteExpense("Rent");
        manager.viewExpenses();
    }
}
