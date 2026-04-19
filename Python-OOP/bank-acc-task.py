from datetime import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "invalid amount"
        self.balance += amount
        self.transactions.append(f"Deposited : {amount} at {datetime.now().strftime('%H:%M:%S')}")
        return self.balance
        
    def withdraw(self, amount):
        if amount <= 0:
            return "invalid amount"
        if amount > self.balance:
            return ("Insufficient balance")            
        self.balance -= amount
        self.transactions.append(f"Withdrew : {amount} at {datetime.now().strftime('%H:%M:%S')}")
        return self.balance

    def transaction_history(self):
        return self.transactions
        
    def check_balance(self):
        return self.balance

name = input("Enter your name : ")
balance = int(input("Enter your balance : "))
print(f"Account created for {name}. balance is {balance}\n")
user = BankAccount(name, balance)

print("Choose any options")
print("1. Deposit")
print("2. Withdraw")
print("3. Check balance")
print("4. Transaction history")
print("5. Exit")

while True:
    choice = input("Enter your choice : ")

    if choice == "1":
        dep_amount = int(input("Enter your deposit amount : "))
        user.deposit(dep_amount)
        print(f"Deposit amount : {dep_amount}")
        print(f"Current balance : {user.check_balance()}")
    elif choice == "2":
        with_amount = int(input("Enter your withdraw amount : "))
        with_status = user.withdraw(with_amount)
        print(with_status)
        print(f"withdraw amount : {with_amount}")
        print(f"Current balance : {user.check_balance()}")
    elif choice == "3":
        print(f"Current balance : {user.check_balance()}")
    elif choice == "4":
        print(f"Transaction history : {user.transaction_history()}")
        print("last three transaction.")
        last_three = user.transaction_history()[-3:]
        for i in last_three:
            print(i)
    elif choice == "5":
        print("Thank you for using our service!")
        break
    else:
        print("Invalid")



