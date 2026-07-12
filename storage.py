import json
import os

DATA_DIR = "data"
JSON_FILE = os.path.join(DATA_DIR, "expenses.json")

os.makedirs(DATA_DIR, exist_ok=True)


def load_expenses():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)