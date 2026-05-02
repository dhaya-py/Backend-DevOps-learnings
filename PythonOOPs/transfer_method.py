# Abstraction

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

    def transfer(self, target_account, amount):
        if self is target_account:
            return False, "Cannot transfer to same account"

        if not isinstance(target_account, BankAccount):
            return False, "Invalid target account"

        status, result = self.withdraw(amount)

        if not status:
            return False, result
        
        status1, result1 = target_account.deposit(amount)
        
        if not status1:
            self.deposit(amount)
            return False, "Failed to deposit in target account"
        return True, "Transfer successful"


acc1 = BankAccount("Dhaya", 5000)
acc2 = BankAccount("Kavya", 5000)

status, result = acc1.transfer(acc2, 5000)
print(result)
print(acc1.check_balance())
print(acc2.check_balance())
print(acc1.transaction_history())
print(acc2.transaction_history())

"""
================================================================================
OOP Concepts & `transfer` Method Workflow Explanation
================================================================================

1. Abstraction & Encapsulation:
   - The BankAccount class hides its internal data fields (`__balance` and `__transactions`) 
     using double underscores (private access modifier).
   - Data is manipulated only through public methods like `deposit`, `withdraw`, 
     `transaction_history`, and `transfer`, ensuring controlled access (Encapsulation).

2. The `transfer` Method (Object Interaction):
   Definition: The `transfer` method allows an object to interact with another object 
   of the same class to safely exchange data (money/balance).

   Workflow:
   Step 1: Validation
     - It checks if the target account is the same as the source account (`self is target_account`).
     - It verifies if the target account is actually an instance of `BankAccount` 
       using `isinstance()`.

   Step 2: Withdrawal from Source
     - It calls `self.withdraw(amount)` to deduct funds from the current object.
     - Automatically logs a "Withdrew" transaction in the source account's history.
     - If withdrawal fails (e.g., insufficient funds), it safely exits and returns False.

   Step 3: Deposit to Target
     - It calls `target_account.deposit(amount)` to add funds to the target object.
     - Automatically logs a "Deposited" transaction in the target account's history.

   Step 4: Rollback Mechanism (Safety/Error Handling)
     - If the deposit into the target account fails for any reason, it triggers a rollback.
     - It calls `self.deposit(amount)` to refund the deducted amount back to the source account,
       ensuring no money is lost during an unexpected failure.

3. Flow of Execution (Example):
   - acc1.transfer(acc2, 5000) -> Method invoked on acc1, targeting acc2.
     -> acc1.withdraw(5000) -> Success (acc1 balance becomes 0).
     -> acc2.deposit(5000)  -> Success (acc2 balance becomes 10000).
     -> Returns True, "Transfer successful".
"""
