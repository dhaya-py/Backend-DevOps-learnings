from datetime import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance # private
        self._transactions = []

    def deposit(self, amount):
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
        if acc_type == "Savings" or acc_type == "savings":
            acc = SavingsAccount(name, balance)
            self.accounts[f"A{len(self.accounts)+1}"] = acc
        elif acc_type == "Current" or acc_type =="current":
            acc = CurrentAccount(name, balance)
            self.accounts[f"A{len(self.accounts)+1}"] = acc
        else:
            return False, {"error" : "INVALID_ACCOUNT_TYPE"}
        return True, {"message" : f"Account created successfully. Account id is {len(self.accounts)}"}

    def get_account(self, acc_id):
        acc = self.accounts.get(acc_id)
        return acc

    def get_account_info(self, acc_id):
        acc = self.get_account(acc_id)
        if not acc:
            return False, {"error" : "ACCOUNT_NOT_FOUND"}
        return True, {
            "message" : "Account found",
            "account_id" : acc_id,
            "name" : acc.name,
            "balance" : acc.get_balance()
        }

    def deposit(self, acc_id, amount):
        acc = self.get_account(acc_id)
        if not acc:
            return False, {"error" : "ACCOUNT_NOT_FOUND"}
        
        status, result = acc.deposit(amount)
        if not status:
            return False, {"error" : "INVALID_AMOUNT"}
        return True, {"message" : "Deposit successful", "data": result}
            

    def withdraw(self, acc_id, amount):
        acc = self.get_account(acc_id)
        if not acc:
            return False, {"error" : "ACCOUNT_NOT_FOUND"} 
        
        status, result = acc.withdraw(amount)
        if not status:
            return False, {"error" : "INSUFFICIENT_BALANCE"}
        return True, {"message" : "Withdrawal successful", "data": result}

    def get_balance(self, acc_id):
        acc = self.get_account(acc_id)
        if acc is None:
            return False, {"error" : "ACCOUNT_NOT_FOUND"}
        return True, {"message" : "Account balance", "data": acc.get_balance()}
    
    def transfer(self, from_acc_id, to_acc_id, amount):
        from_acc = self.get_account(from_acc_id)
        if from_acc is None:
            return False, {"error" : "FROM_ACCOUNT_NOT_FOUND"}
        to_acc = self.get_account(to_acc_id)
        if to_acc is None:
            return False, {"error" : "TO_ACCOUNT_NOT_FOUND"}

        status, result = from_acc.withdraw(amount)
        if status is False:
            return False, {"error" : "INSUFFICIENT_BALANCE"}

        status, result = to_acc.deposit(amount)
        if status is False:
            from_acc.deposit(amount)
            return False, {"error" : "INVALID_AMOUNT"}
        return True, {"message" : "Transfer successful", "data": result}

    def statement(self, acc_id):
        acc = self.get_account(acc_id)
        if not acc:
            return False, {"error" : "ACCOUNT_NOT_FOUND"}
        return True, {
            "message" : "Statement of the account",
            "transactions" : acc.get_transaction(),
            "balance" : acc.get_balance()
        }