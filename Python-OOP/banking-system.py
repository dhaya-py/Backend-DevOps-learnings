
# Inheritance + Ploymorphism

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

acc1 = SavingsAccount("Dhaya", 5000)
print(acc1.deposit(5000))
print(acc1.withdraw(2000))
print(acc1.get_transaction())
print(acc1.get_balance())

acc2 = CurrentAccount("Dhaya", 5000)
print(acc2.deposit(5000))
print(acc2.withdraw(2000))
print(acc2.get_transaction())
print(acc2.get_balance())

print(acc1.withdraw(6000))

print(acc2.withdraw(6000))


"""
*** NOTES & DEFINITIONS ***

1. Inheritance:
   - A mechanism where a new class (child/subclass) derives properties and behaviors (methods) 
     from an existing class (parent/superclass).
   - `class SavingsAccount(BankAccount):` and `class CurrentAccount(BankAccount):`
     Here, SavingsAccount and CurrentAccount inherit from BankAccount. This means they get 
     `deposit()`, `withdraw()`, `get_balance()`, etc., without rewriting the code!
   - `super().__init__(name, balance)`: The `super()` function allows a subclass to call methods 
     from its parent class. Here, it calls the parent's constructor to set up `name`, `_balance`, 
     and `_transactions` properly.

2. Polymorphism (Method Overriding):
   - Polymorphism means "many forms". In OOP, it allows subclasses to provide a specific 
     implementation of a method that is already defined in its parent class.
   - `withdraw()` in `BankAccount` vs `withdraw()` in `CurrentAccount`: 
     Both classes have a `withdraw` method, but `CurrentAccount` provides its own specific 
     implementation (overriding the parent's method) to include the overdraft logic 
     (`amount > self._balance + self.__overdraft`).
     When you call `acc2.withdraw()`, Python knows to use the `CurrentAccount` version!

3. Access Modifiers (Protected vs Private):
   - `self._balance` & `self._transactions`: Changed from double underscore `__` to single 
     underscore `_`. A single underscore implies the variable is "protected". It shouldn't be 
     accessed directly from outside the class, but it *is* intended to be accessible to and 
     modified by subclasses (like SavingsAccount and CurrentAccount).
"""
