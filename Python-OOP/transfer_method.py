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
