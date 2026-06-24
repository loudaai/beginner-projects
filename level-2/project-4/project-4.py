import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "transaction.json"


def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(transactions):
    with open(FILE_PATH, "w") as file:
        json.dump(transactions, file)


def add_transaction(transactions, transaction_type):
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date: ")

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date
    }

    transactions.append(transaction)
    print(f"{transaction_type.capitalize()} added.")


def view_transactions(transactions):
    if len(transactions) == 0:
        print("No transactions yet.")
        return

    print("\nTransactins:")

    for transaction in transactions:
        print(
            f"{transaction['date']} | "
            f"{transaction['type']} | "
            f"{transaction['category']} | "
            f"{transaction['amount']}"
        )


def view_summary(transactions):
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        elif transaction["type"] == "expense":
            total_expense += transaction["amount"]

    balance = total_income - total_expense

    print("\nSummary")
    print(f"Total income: {total_income}")
    print(f"Total expense: {total_expense}")
    print(f"Balance: {balance}")


def find_by_category(transactions):
    category_search = input("Enter category: ")
    found = False

    for transaction in transactions:
        if transaction["category"].lower() == category_search.lower():
            print(
                f"{transaction['date']} | "
                f"{transaction['type']} | "
                f"{transaction['category']} | "
                f"{transaction['amount']}"
            )

            found = True

    if found == False:
        print("No transactions found in that category.")


def show_menu():
    print("\nPersonal Finance Dashboard")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")
    print("5. Find by category")
    print("6. Save and exit")


transactions = load_data()


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_transaction(transactions, "income")

    elif choice == "2":
        add_transaction(transactions, "expense")

    elif choice == "3":
        view_transactions(transactions)

    elif choice == "4":
        view_summary(transactions)

    elif choice == "5":
        find_by_category(transactions)

    elif choice == "6":
        save_data(transactions)
        print("Data saved. Goodbye!")
        break

    else:
        print("invalid choice")
