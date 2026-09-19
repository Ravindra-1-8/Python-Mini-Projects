# PyBank - Simple Banking App.

# Features:

# 1. Deposit money (supports decimal amounts)
# 2. Withdraw money (cannot exceed available balance)
# 3. Check current balance.
# 4. View transaction history.
# 5. Show total deposits and withdrawal.
# 6. Menu-based navigation with confirmation messages.
# 7. Exit option to close the program.

balance = 0.0
transactions = [] # for storing transaction

def deposit(amount):
    global balance

    balance += amount
    transactions.append(f"Deposit {amount}/-")
    print(f"{amount} deposited successfully.")

def withdraw(amount):
    global balance

    if amount > balance:
        print("Sorry, you cannot withdraw more than you have.")
    else:
        balance -= amount
        transactions.append(f"Withdrawn {amount}/-")
        print(f"{amount} withdred successfully.\n")

def checkBalance():
    global balance
    print(f"Current balance: {balance}\n")

def transactionhistory():
    if not transactions:
        print("no transactions yet.\n")
    else:
        print("-----------Transaction History------------")

        for t in transactions:
            print("\n-", t)
        deposits = sum(1 for t in transactions if 'Deposited' in t)
        withdraws = sum(1 for t in transactions if 'Withdrawn' in t)
        print(f"\n Total deposited: {deposits}\n")
        print(f" Total withdrawn: {withdraws}\n")

def menu():
    while True:
        print("-------------PyBank--------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter your deposit amount: "))
            deposit(amount)

        elif choice == "2":
            amount = float(input("Enter your withdrawal amount: "))
            withdraw(amount)

        elif choice == "3":
            checkBalance()

        elif choice == "4":
            transactionhistory()

        elif choice == "5":
            print("Thank you for your time!")
            break

        else:
            print("Sorry, please enter a valid choice.")

menu()