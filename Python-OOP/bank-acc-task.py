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

"""
*** NOTES & DEFINITIONS ***

1. Classes & Objects:
   - Class (`BankAccount`): A blueprint for creating objects. 
     It defines the properties (attributes) and behaviors (methods) 
     that the objects will have.

   - Object (`user`): An instance of the `BankAccount` class created 
     using `user = BankAccount(name, balance)`. 
     It represents a specific bank account with its own state.

2. Methods:
   - These are functions defined inside a class that operate on instances of that class
     (e.g., `deposit()`, `withdraw()`, `check_balance()`).

   - `__init__`: The constructor method. It automatically runs when a new object
     is created and is used to initialize the object's attributes.

3. Encapsulation (Private Variables):
   - The concept of bundling data and methods that work on that data within one unit 
     and restricting direct access to some of the object's components.

   - Private Variables (`__balance`, `__transactions`): Prefixed with double underscores `__`. 
     This makes them inaccessible directly from outside the class 
     (e.g., `user.__balance` would raise an error). 
     They can only be modified through the class methods, protecting the data 
     from unwanted external changes.

4. Dictionaries for Transactions:
   - Instead of storing simple strings, transactions are stored as dictionaries
     `{"id": ..., "type": ..., "amount": ..., "time": ...}`. 
     This is a structured way to store complex records, allowing you to easily 
     access individual pieces of data (e.g., `transaction['amount']`).

5. Dynamic Record Keeping (Timestamp & IDs):
   - `datetime.now().strftime('%H:%M')`: Uses the built-in `datetime` module to 
     capture the exact time a transaction occurs and formats it as Hour:Minute.
     
   - `f"T{len(self.__transactions)+1}"`: Dynamically generates a unique 
     transaction ID based on the current number of transactions (e.g., T1, T2, T3).
"""

