import csv

FILE = "expenses.csv"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    note = input("Enter note (optional): ")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!")


def view_expenses():
    total = 0

    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)

            print("\nDate\t\tCategory\tAmount\tNote")
            print("-" * 50)

            for row in reader:
                print(f"{row[0]}\t{row[1]}\t\t₹{row[2]}\t{row[3]}")
                total += float(row[2])

            print("-" * 50)
            print("Total Spent: ₹", total)

    except FileNotFoundError:
        print("No expenses recorded yet.")


def category_summary():
    summary = {}

    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                category = row[1]
                amount = float(row[2])

                summary[category] = summary.get(category, 0) + amount

        print("\nCategory Wise Spending:")
        for category, amount in summary.items():
            print(category, ": ₹", amount)

    except FileNotFoundError:
        print("No expenses recorded yet.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")