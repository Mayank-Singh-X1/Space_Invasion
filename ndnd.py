import json
import os

class Transaction:
    def __init__(self, t_type, desc, amount):
        self.t_type = t_type
        self.desc = desc
        self.amount = amount

    def to_dict(self):
        return {'t_type': self.t_type, 'desc': self.desc, 'amount': self.amount}

transactions = []

def add_transaction():
    t_type = input("Enter type (Income/Expense): ")
    desc = input("Enter description: ")
    amount = float(input("Enter amount: "))
    transactions.append(Transaction(t_type, desc, amount))

def list_transactions():
    print("\n--- All Transactions ---")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t.t_type} - {t.desc}: ${t.amount:.2f}")

def save_to_file():
    with open("finance.json", "w") as f:
        json.dump([t.to_dict() for t in transactions], f)
    print("Data saved!")

def load_from_file():
    if not os.path.exists("finance.json"):
        return
    with open("finance.json", "r") as f:
        data = json.load(f)
        for entry in data:
            transactions.append(Transaction(**entry))
    print("Data loaded!")

def filter_expenses_over_100():
    print("\nExpenses > $100:")
    for t in transactions:
        if t.t_type.lower() == "expense" and t.amount > 100:
            print(f"{t.desc}: ${t.amount:.2f}")

def spending_chart():
    print("\n--- ASCII Spending Chart ---")
    for t in transactions:
        if t.t_type.lower() == "expense":
            bars = int(t.amount / 10)
            print(f"{t.desc:20} | {'#'*bars}")

def main():
    load_from_file()
    while True:
        print("\n1. Add Transaction\n2. List Transactions\n3. Filter > $100\n4. Spending Chart\n5. Save\n6. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            filter_expenses_over_100()
        elif choice == "4":
            spending_chart()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            save_to_file()
            break

if __name__ == "__main__":
    main()
