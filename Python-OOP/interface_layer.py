# interface layer


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

class Bank():
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance, acc_type):
        if acc_type == "Savings":
            acc = SavingsAccount(name, balance)
            self.accounts[f"A{len(self.accounts)+1}"] = acc
        elif acc_type == "Current":
            acc = CurrentAccount(name, balance)
            self.accounts[f"A{len(self.accounts)+1}"] = acc
        else:
            return False, "Invalid Account type"
        return True, f"Account created successfully. Account id is A{len(self.accounts)}"

    def get_account(self, acc_id):
        if acc_id in self.accounts:
            return True, self.accounts.get(acc_id)
        return False, "Account not found"

    def deposit(self, acc_id, amount):
        status, acc = self.get_account(acc_id)
        if not status:
            return False, acc
        return acc.deposit(amount)

    def withdraw(self, acc_id, amount):
        status, acc = self.get_account(acc_id)
        if not status:
            return False, acc
        return acc.withdraw(amount)
    
    def transfer(self, from_acc_id, to_acc_id, amount):
        status, from_acc = self.get_account(from_acc_id)
        if not status:
            return False, from_acc
        status, to_acc = self.get_account(to_acc_id)
        if not status:
            return False, to_acc

        status, result = from_acc.withdraw(amount)
        if not status:
            return False, result

        status, result = to_acc.deposit(amount)
        if not status:
            from_acc.deposit(amount)
            return False, result
        return True, "Transfer successful"
        

bank = Bank()
print(bank.create_account("Dhaya", 5000, "Savings"))
print(bank.create_account("Kavya", 5000, "Current"))
print(bank.deposit("A1", 5000))
print(bank.withdraw("A2", 5000))
print(bank.transfer("A1","A2", 5000))

print(bank.get_account("A1"))
print(bank.get_account("A2"))
print(bank.get_account("A3"))


"""
================================================================================
# OOP Concepts & Implementation Notes: Bank Interface Layer
================================================================================

--- 1. Definitions & Concepts ---
* Encapsulation: Restricting direct access to data.
  - Protected (_balance): Intended as private, but accessible in subclasses.
  - Private (__overdraft): Strictly hidden, preventing accidental external modification.
* Inheritance: Creating specialized classes from a base class.
  - SavingsAccount and CurrentAccount inherit core logic from BankAccount.
* Polymorphism (Method Overriding): Modifying inherited behavior.
  - CurrentAccount overrides the `withdraw` method to handle overdraft limits.
* Facade Pattern / Interface Layer: Providing a simplified, unified interface.
  - The `Bank` class acts as an interface, handling account retrieval and delegating tasks to specific account objects.

--- 2. Workflows ---
* Account Creation (Bank.create_account):
  1. Instantiates a Savings or Current account based on `acc_type`.
  2. Generates a unique ID (e.g., "A1") and stores the object in `self.accounts`.

* Unified Transactions (Bank.deposit / Bank.withdraw):
  1. Fetches the target account object using its ID.
  2. Delegates the operation to the object's specific `deposit` or `withdraw` method.

* Inter-Account Transfer (Bank.transfer):
  1. Validates the existence of both the sender and receiver accounts.
  2. Attempts withdrawal from the sender. Aborts if it fails.
  3. Attempts deposit into the receiver. 
  4. Rollback: If the deposit fails, refunds the withdrawn amount back to the sender.
================================================================================
"""