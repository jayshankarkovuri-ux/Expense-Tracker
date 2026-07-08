def display_menu():
    print("=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Save Expenses")
    print("6. Exit")
    print("=" * 40)


expenses = []

while True:

    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter Expense Name: ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        expense = {
            "title": title,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added Successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\nYour Expenses:\n")

            for expense in expenses:
                print("---------------------")
                print("Title :", expense["title"])
                print("Category :", expense["category"])
                print("Amount :", expense["amount"])

    elif choice == "3":
        print("Search Expense Selected")

    elif choice == "4":
        print("Delete Expense Selected")

    elif choice == "5":
        print("Save Expenses Selected")

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice")