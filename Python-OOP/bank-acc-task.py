from datetime import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # private
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False, "invalid amount"
        self.__balance += amount
        transaction = {
            "id" : f"T{len(self.__transactions)+1}",
            "type" : "Deposited",
            "amount" : amount,
            "time" : datetime.now().strftime('%H:%M')
        }
        self.__transactions.append(transaction)
        return True, self.__balance
        
    def withdraw(self, amount):
        if amount <= 0:
            return False, "invalid amount"
        if amount > self.__balance:
            return False, "Insufficient balance"           
        self.__balance -= amount
        transaction = {
            "id" : f"T{len(self.__transactions)+1}",
            "type" : "Withdrew",
            "amount" : amount,
            "time" : datetime.now().strftime('%H:%M')
        }
        self.__transactions.append(transaction)
        return True, self.__balance

    def transaction_history(self):
        return self.__transactions.copy()
        
    def check_balance(self):
        return self.__balance

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
        status, result = user.deposit(dep_amount)
        print(f"Deposit amount : {dep_amount}")
        if status:
            print(f"Success. Current balance : {result}")
        else:
            print(f"Error : {result}")

    elif choice == "2":
        with_amount = int(input("Enter your withdraw amount : "))
        status, result = user.withdraw(with_amount)
        print(f"withdraw amount : {with_amount}")
        if status:
            print(f"Success. Current balance : {result}")
        else:
            print(f"Error : {result}")

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



