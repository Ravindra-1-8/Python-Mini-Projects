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

# for storing transaction.
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposit {amount}/-")
    print(f"{amount} deposited successfully.")

def menu():
    while True:
        printt("-------------PyBank--------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            checkBalance()
        elif choice == "4":
            transactionhistory()
        elif choice == "5":
            print("Thank you for your time!")
            break
        else:
            print("Sorry, please enter a valid choice.")