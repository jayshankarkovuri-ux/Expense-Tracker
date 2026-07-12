import json

# Load expenses from JSON file
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
    print("Expenses Loaded Successfully!")
except FileNotFoundError:
    expenses = []


def display_menu():
    print("\n" + "=" * 40)
    print("         EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Save Expenses")
    print("6. Summary Report")
    print("7. Category Analysis")
    print("8. Monthly Report")
    print("9. Sort Expenses")
    print("10. Exit")
    print("=" * 40)


def display_summary():
    total_expenses = len(expenses)

    total_amount = sum(expense["amount"] for expense in expenses)

    if total_expenses > 0:
        average_expense = total_amount / total_expenses
        highest_expense = max(expense["amount"] for expense in expenses)
    else:
        average_expense = 0
        highest_expense = 0

    print("\nSUMMARY REPORT")
    print("-" * 30)
    print(f"Total Expenses : {total_expenses}")
    print(f"Total Amount   : ₹{total_amount}")
    print(f"Average Expense: ₹{average_expense:.2f}")
    print(f"Highest Expense: ₹{highest_expense}")


def category_analysis():

    if len(expenses) == 0:
        print("No expenses available.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"].lower()
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nCATEGORY ANALYSIS")
    print("-" * 30)

    for category, total in category_totals.items():
        print(f"{category.title()}: ₹{total}")


def monthly_report():

    month = input("Enter Month (YYYY-MM): ")

    total = 0

    print("\nMONTHLY REPORT")
    print("-" * 30)

    found = False

    for expense in expenses:

        if expense.get("date", "").startswith(month):

            print(
                f"{expense['title']} | "
                f"{expense['category']} | "
                f"{expense['date']} | "
                f"₹{expense['amount']}"
            )

            total += expense["amount"]
            found = True

    if found:
        print("-" * 30)
        print(f"Total Monthly Expense: ₹{total}")
    else:
        print("No expenses found for this month.")


def sort_expenses():

    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n1. Sort by Amount (Low to High)")
    print("2. Sort by Amount (High to Low)")

    option = input("Choose option: ")

    if option == "1":
        sorted_expenses = sorted(
            expenses,
            key=lambda expense: expense["amount"]
        )

    elif option == "2":
        sorted_expenses = sorted(
            expenses,
            key=lambda expense: expense["amount"],
            reverse=True
        )

    else:
        print("Invalid Choice!")
        return

    print("\nSORTED EXPENSES")
    print("-" * 40)

    for expense in sorted_expenses:

        print(f"Title    : {expense['title']}")
        print(f"Category : {expense['category']}")
        print(f"Date     : {expense.get('date', 'N/A')}")
        print(f"Amount   : ₹{expense['amount']}")
        print("-" * 40)


while True:

    display_menu()

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":

        title = input("Enter Expense Title: ")
        category = input("Enter Category: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid Amount!")
            continue

        expense = {
            "title": title,
            "category": category,
            "date": date,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added Successfully!")

    # View Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\nEXPENSE LIST")
            print("-" * 40)

            for expense in expenses:

                print(f"Title    : {expense['title']}")
                print(f"Category : {expense['category']}")
                print(f"Date     : {expense.get('date', 'N/A')}")
                print(f"Amount   : ₹{expense['amount']}")
                print("-" * 40)

    # Search Expense
    elif choice == "3":

        search = input("Enter Expense Name: ")

        found = False

        for expense in expenses:

            if expense["title"].lower() == search.lower():

                print("\nExpense Found!")
                print(f"Title    : {expense['title']}")
                print(f"Category : {expense['category']}")
                print(f"Date     : {expense.get('date', 'N/A')}")
                print(f"Amount   : ₹{expense['amount']}")

                found = True
                break

        if not found:
            print("Expense Not Found!")

    # Delete Expense
    elif choice == "4":

        delete_name = input("Enter Expense Name to Delete: ")

        found = False

        for expense in expenses:

            if expense["title"].lower() == delete_name.lower():

                expenses.remove(expense)

                print("Expense Deleted Successfully!")

                found = True
                break

        if not found:
            print("Expense Not Found!")

    # Save Expenses
    elif choice == "5":

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expenses Saved Successfully!")

    # Summary Report
    elif choice == "6":

        display_summary()

    # Category Analysis
    elif choice == "7":

        category_analysis()

    # Monthly Report
    elif choice == "8":

        monthly_report()

    # Sort Expenses
    elif choice == "9":

        sort_expenses()

    # Exit
    elif choice == "10":

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")