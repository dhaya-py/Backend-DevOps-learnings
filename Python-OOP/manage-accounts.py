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