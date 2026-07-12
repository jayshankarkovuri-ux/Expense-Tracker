import matplotlib.pyplot as plt
import csv
import os
from storage import load_expenses, save_expenses

REPORTS_DIR = "reports"
CSV_FILE = os.path.join(REPORTS_DIR, "expenses.csv")
os.makedirs(REPORTS_DIR, exist_ok=True)

expenses = load_expenses()
budget_limit = 0.0


def display_menu():
    print("\n" + "=" * 45)
    print("              EXPENSE TRACKER")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Save Expenses")
    print("6. Summary Report")
    print("7. Category Analysis")
    print("8. Sort Expenses by Amount (High to Low)")
    print("9. Sort Expenses by Amount (Low to High)")
    print("10. Sort Expenses by Title")
    print("11. Highest and Lowest Expense")
    print("12. Export Expenses to CSV")
    print("13. Set Budget")
    print("14. Check Budget Status")
    print("15. Generate Expense Chart")
    print("16. Exit")


def display_expenses(expense_list):
    if not expense_list:
        print("No expenses found.")
        return

    print("\nEXPENSE LIST")
    print("-" * 45)
    for expense in expense_list:
        print(f"Title    : {expense['title']}")
        print(f"Category : {expense['category']}")
        print(f"Amount   : ₹{expense['amount']}")
        print("-" * 45)


def summary_report():
    total_expenses = len(expenses)
    total_amount = sum(expense["amount"] for expense in expenses)

    if total_expenses > 0:
        average_expense = total_amount / total_expenses
        highest_expense = max(expense["amount"] for expense in expenses)
    else:
        average_expense = 0
        highest_expense = 0

    print("\nSUMMARY REPORT")
    print("-" * 45)
    print(f"Total Expenses  : {total_expenses}")
    print(f"Total Amount    : ₹{total_amount}")
    print(f"Average Expense : ₹{average_expense:.2f}")
    print(f"Highest Expense : ₹{highest_expense}")


def category_analysis():
    if not expenses:
        print("No expenses found.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense["category"].strip().lower()
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\nCATEGORY ANALYSIS")
    print("-" * 45)
    for category, total in category_totals.items():
        print(f"{category.title():<20} ₹{total}")
    print("-" * 45)
    print(f"Total Amount: ₹{sum(category_totals.values())}")


def highest_and_lowest_expense():
    if not expenses:
        print("No expenses found.")
        return

    highest = max(expenses, key=lambda x: x["amount"])
    lowest = min(expenses, key=lambda x: x["amount"])

    print("\nHIGHEST AND LOWEST EXPENSE")
    print("-" * 45)
    print("Highest Expense:")
    print(f"Title    : {highest['title']}")
    print(f"Category : {highest['category']}")
    print(f"Amount   : ₹{highest['amount']}")
    print("-" * 45)
    print("Lowest Expense:")
    print(f"Title    : {lowest['title']}")
    print(f"Category : {lowest['category']}")
    print(f"Amount   : ₹{lowest['amount']}")
    print("-" * 45)


def export_to_csv():
    if not expenses:
        print("No expenses to export.")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported successfully to {CSV_FILE}")


def set_budget():
    global budget_limit
    try:
        budget_limit = float(input("Enter Monthly Budget: ₹"))
        if budget_limit < 0:
            print("Budget cannot be negative.")
            budget_limit = 0
            return
        print(f"Budget set successfully! Budget = ₹{budget_limit}")
    except ValueError:
        print("Invalid budget amount!")


def check_budget():
    if budget_limit <= 0:
        print("Please set a budget first!")
        return

    total_expenses = sum(expense["amount"] for expense in expenses)

    print("\nBUDGET STATUS")
    print("-" * 45)
    print(f"Budget Limit : ₹{budget_limit}")
    print(f"Total Spent  : ₹{total_expenses}")

    if total_expenses > budget_limit:
        print("WARNING: Budget Exceeded!")
        print(f"Exceeded By: ₹{total_expenses - budget_limit}")
    else:
        print("Budget is under control")
        print(f"Remaining Budget: ₹{budget_limit - total_expenses}")


def sort_by_amount(reverse=True):
    if not expenses:
        print("No expenses found.")
        return
    sorted_expenses = sorted(expenses, key=lambda x: x["amount"], reverse=reverse)
    display_expenses(sorted_expenses)


def sort_by_title():
    if not expenses:
        print("No expenses found.")
        return
    sorted_expenses = sorted(expenses, key=lambda x: x["title"].lower())
    display_expenses(sorted_expenses)

    

def generate_expense_chart():
    if not expenses:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"].strip().title()
        amount = expense["amount"]

        category_totals[category] = category_totals.get(category, 0) + amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    os.makedirs("images", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts)

    plt.title("Expense Tracker - Category Wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.tight_layout()

    plt.savefig("images/expense_chart.png")
    plt.show()
    plt.close()

    print("Chart saved successfully in images/expense_chart.png")
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter Expense Title: ").strip()
        category = input("Enter Category: ").strip()

        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        expense = {
            "title": title,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense Added Successfully!")

    elif choice == "2":
        display_expenses(expenses)

    elif choice == "3":
        search = input("Enter Expense Name: ").strip()
        found = False

        for expense in expenses:
            if expense["title"].lower() == search.lower():
                print("\nExpense Found!")
                print("-" * 45)
                print(f"Title    : {expense['title']}")
                print(f"Category : {expense['category']}")
                print(f"Amount   : ₹{expense['amount']}")
                found = True
                break

        if not found:
            print("Expense Not Found!")

    elif choice == "4":
        delete_name = input("Enter Expense Name to Delete: ").strip()
        found = False

        for expense in expenses:
            if expense["title"].lower() == delete_name.lower():
                expenses.remove(expense)
                print("Expense Deleted Successfully!")
                found = True
                break

        if not found:
            print("Expense Not Found!")

    elif choice == "5":
        save_expenses(expenses)
        print("Expenses Saved Successfully!")

    elif choice == "6":
        summary_report()

    elif choice == "7":
        category_analysis()

    elif choice == "8":
        sort_by_amount(reverse=True)

    elif choice == "9":
        sort_by_amount(reverse=False)

    elif choice == "10":
        sort_by_title()

    elif choice == "11":
        highest_and_lowest_expense()

    elif choice == "12":
        export_to_csv()

    elif choice == "13":
        set_budget()

    elif choice == "14":
        check_budget()

    elif choice == "15":
        generate_expense_chart()

    elif choice == "16":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")