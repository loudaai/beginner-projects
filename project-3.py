expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spent")
    print("4. Show expense by category")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        category = input("Category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet")
        else:
            print("\nYour expenses:")

            for expense in expenses:
                print(
                    f"{expense['name']} - {expense['amount']} - {expense['category']}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense['amount']

        print(f"total spent: {total}")

    elif choice == "4":
        category_search = input("Enter category: ")

        found = False

        for expense in expenses:
            if expense['category'].lower() == category_search.lower():
                print(f"{expense['name']} - {expense['amount']}")
                found = True

        if not found:
            print("No expenses found in that category")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
