import json


def display_menu():
    print("=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Save Expenses")
    print("6. Exit")
    print("=" * 40)


def load_expenses(path="expenses.json"):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


expenses = load_expenses()


while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter Title: ").strip()
        category = input("Enter Category: ").strip()
        try:
            amount = float(input("Enter Amount: ").strip())
        except ValueError:
            print("Invalid amount.")
            continue
        expense = {"title": title, "category": category, "amount": amount}
        expenses.append(expense)
        print("Expense Added Successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:\n")
            for e in expenses:
                print("------------------------")
                print("Title :", e.get("title"))
                print("Category :", e.get("category"))
                print("Amount :", e.get("amount"))

    elif choice == "3":
        search = input("Enter Expense Name: ").strip()
        found = False
        for expense in expenses:
            if expense.get("title", "").lower() == search.lower():
                print("\nExpense Found!")
                print("------------------------")
                print("Title :", expense.get("title"))
                print("Category :", expense.get("category"))
                print("Amount :", expense.get("amount"))
                found = True
                break
        if not found:
            print("Expense Not Found!")

    elif choice == "4":
        delete_name = input("Enter Expense Name to Delete: ").strip()
        found = False
        for expense in list(expenses):
            if expense.get("title", "").lower() == delete_name.lower():
                expenses.remove(expense)
                print("\nExpense Deleted Successfully!")
                found = True
                break
        if not found:
            print("Expense Not Found!")

    elif choice == "5":
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("\nExpenses Saved Successfully!")

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice")