import json

with open("expenses.json", "r") as file:
    expenses = json.load(file)

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("\nExpense Analysis")
print("-" * 30)

total_expense = 0

for category, total in category_totals.items():
    print(f"{category}: ₹{total}")
    total_expense += total

print("-" * 30)
print(f"Total Expenses: ₹{total_expense}")