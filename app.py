import json
import csv
import os

DATA_DIR = "data"
REPORTS_DIR = "reports"
JSON_FILE = os.path.join(DATA_DIR, "expenses.json")
CSV_FILE = os.path.join(REPORTS_DIR, "expenses.csv")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


def load_expenses():
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                print("Expenses Loaded Successfully!")
                return data
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_expenses():
    with open(JSON_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Expenses Saved Successfully!")


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
    print("13. Exit")
    print("=" * 45)


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

    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported successfully to {CSV_FILE}")


expenses = load_expenses()

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
        save_expenses()

    elif choice == "6":
        summary_report()

    elif choice == "7":
        category_analysis()

    elif choice == "8":
        if not expenses:
            print("No expenses found.")
        else:
            sorted_expenses = sorted(expenses, key=lambda x: x["amount"], reverse=True)
            display_expenses(sorted_expenses)

    elif choice == "9":
        if not expenses:
            print("No expenses found.")
        else:
            sorted_expenses = sorted(expenses, key=lambda x: x["amount"])
            display_expenses(sorted_expenses)

    elif choice == "10":
        if not expenses:
            print("No expenses found.")
        else:
            sorted_expenses = sorted(expenses, key=lambda x: x["title"].lower())
            display_expenses(sorted_expenses)

    elif choice == "11":
        highest_and_lowest_expense()

    elif choice == "12":
        export_to_csv()

    elif choice == "13":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")