from datetime import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance # private
        self._transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False, "invalid amount"
        self._balance += amount
        transaction = {
            "id" : f"T{len(self._transactions)+1}",
            "type" : "Deposited",
            "amount" : amount,
            "time" : datetime.now().strftime('%H:%M')
        }
        self._transactions.append(transaction)
        return True, self._balance
        
    def withdraw(self, amount):
        if amount <= 0:
            return False, "invalid amount"
        if amount > self._balance:
            return False, "Insufficient balance"           
        self._balance -= amount
        transaction = {
            "id" : f"T{len(self._transactions)+1}",
            "type" : "Withdrew",
            "amount" : amount,
            "time" : datetime.now().strftime('%H:%M')
        }
        self._transactions.append(transaction)
        return True, self._balance

    def get_transaction(self):
        return self._transactions.copy()
        
    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def add_interest(self, interest):
        interest = self._balance * interest / 100
        self._balance += interest
        return True, self._balance


class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft=5000):
        super().__init__(name, balance)
        self.__overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Invalid amount"
        if amount > self._balance + self.__overdraft:
            return False, "Insufficient balance. overdraft limit exceeded"
        self._balance -= amount
        transaction = {
            "id" : f"T{len(self._transactions)+1}",
            "type" : "Withdrew",
            "amount" : amount,
            "time" : datetime.now().strftime('%H:%M')
        }
        self._transactions.append(transaction)
        return True, self._balance

class Bank(BankAccount):
    def __Init__(self, name, balance):
        super().__init__(name, balance)
        self.accounts = []

    def create_account(self, name, balance, acc_type):
        if acc_type == "Savings":
            acc = SavingsAccount(name, balance)
        elif acc_type == "Current":
            acc = CurrentAccount(name, balance)
        else:
            return False, "Invalid Accoiunt Type"
        self.accounts.append(acc)
        return True, acc

    def get_account(self, name):
        for acc in self.accounts:
            if acc.name == name:
                return acc
        return None

bank = Bank("Dhaya", 5000)
bank.create_account("user1", 5000, "Savings")
bank.create_account("user2", 5000, "Current")

user1 = bank.get_account("user1")
user2 = bank.get_account("user2")

print(user1.deposit(5000))
print(user2.withdraw(5000))
print(user1.get_transaction())
print(user2.get_transaction())


"""
*** NOTES & DEFINITIONS ***

1. Object Composition (Aggregation):
   - Definition: The concept of classes containing objects of other classes.
   - Example: The `Bank` class is designed to store and manage multiple accounts.
   - Logic: `self.accounts = []` is used to hold instances of `SavingsAccount` and `CurrentAccount`. 
   The Bank object "has a" collection of Account objects.

2. Workflow: Account Creation (Factory Logic):
   - `create_account(self, name, balance, acc_type)` acts as an object factory.
   - Logic: It checks the `acc_type` string using `if/elif`. 
   Based on the string, it conditionally instantiates either a `SavingsAccount` or 
   a `CurrentAccount`.
   - Result: The newly created object (`acc`) is appended to the `self.accounts` list, 
   successfully registering it in the Bank's central system.

3. Workflow: Account Retrieval (Search Logic):
   - `get_account(self, name)` fetches an existing account for future transactions.
   - Logic: It uses a `for` loop to iterate over the `self.accounts` list. 
   It compares the requested `name` against `acc.name`.
   - Result: If a match is found, it returns the specific object reference (e.g., `user1`), allowing you to call `.deposit()` or `.withdraw()` on it directly.

---
💡 OOP Tip for the `Bank` Class:
    - A `Bank` normally shouldn't inherit from `BankAccount` (`class Bank(BankAccount)`), 
    because a Bank *has* accounts, but it *is not* an account itself. 
    - Watch out for a typo on line 75! Python constructors must be lowercase `__init__`, 
    but you have `__Init__`.
"""