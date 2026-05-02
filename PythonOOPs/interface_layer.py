# interface layer


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
        

bank = Bank()
print(bank.create_account("Dhaya", 5000, "Savings"))
print(bank.create_account("Kavya", 5000, "Current"))
print(bank.deposit("A1", 5000))
print(bank.withdraw("A2", 5000))
print(bank.transfer("A1","A2", 5000))

print(bank.get_account_info("A2"))
print(bank.statement("A2"))




"""

1. Interface Layer - Why we need it?
Imagine giving a customer direct access to the engine room of a bank.

No customer should ever interact directly with a SavingsAccount object.

The Bank class acts as a safe "Interface Layer" or "Facade".

It shields the customer from the complexity of different account types and enforces rules.

2. How it strengthens the system
Never touch internal objects directly:
The interface layer ensures all operations pass through standardized methods (deposit, withdraw).

No accidental breaches:
The private __overdraft attribute is protected. Only CurrentAccount's own methods can touch it.

Consistent responses:
Every method now returns the same structure: (Boolean Success, Data/Error).

This makes it predictable for whatever is calling it (like a UI or another program).

Rollback safety:
In transfer, if the second step fails, we automatically reverse the first step. This is critical for data integrity.
"""


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







"""

.

FINAL CLEAN NOTES
1. CORE OOP CONCEPTS (REFINED)

Encapsulation

Control access to data, don’t expose internals

_balance → protected (by convention)
__overdraft → private (name mangling)

Access only via methods:
deposit(), withdraw(), get_balance()

Inheritance
Reuse and extend behavior

SavingsAccount → BankAccount  
CurrentAccount → BankAccount

Polymorphism (REAL understanding)

Same method, different behavior based on object

withdraw() behaves differently for:
- SavingsAccount
- CurrentAccount (overdraft logic)

Abstraction (CRITICAL)

Hide internal complexity, expose simple interface

Wrong:

acc._balance
acc._transactions

Correct:

acc.deposit()
acc.withdraw()

Composition

“Has-a” relationship

Bank HAS accounts

2. INTERFACE LAYER (MOST IMPORTANT)
Definition

Interface layer = how the outside world interacts with your system

Structure:
User → Bank → Account → Data
Responsibilities:
Bank:
create account
store accounts
find accounts
perform operations
Account:
business logic (deposit, withdraw)

Rule:

User should NEVER interact with account objects directly

3. SYSTEM WORKFLOW

Account Creation
User → Bank.create_account()
      ↓
Bank creates object
      ↓
Stores in dictionary
      ↓
Returns account_id

Deposit / Withdraw
User → Bank.deposit(account_id)
      ↓
Bank finds account
      ↓
Calls acc.deposit()
      ↓
Returns result

Transfer
User → Bank.transfer(A1, A2)
      ↓
Bank finds both accounts
      ↓
Withdraw from A1
      ↓
Deposit to A2
      ↓
Rollback if failure

Statement
User → Bank.statement()
      ↓
Returns safe data (not object)

4. KEY DESIGN DECISIONS
Separation of concerns
Method	Role
get_account()	internal (returns object)
get_account_info()	external (safe data)

Return format (STANDARDIZED)

(True, {"message": "...", "data": ...})
(False, {"message": "...", "data": None})

Internal vs External

Type	Purpose
Object	internal logic
Dict	external response

5. ISSUES YOU FACED (IMPORTANT)
Issue 1: AttributeError (method not found)

Cause:

Calling methods that don’t exist

Fix:

Ensure correct class owns method

Issue 2: tuple has no attribute deposit

Cause:

get_account() returned (True, data)

Fix:

Separate:
internal → object
external → dict

Issue 3: Breaking abstraction

Cause:

accessing __transactions directly

Fix:

Use methods only

Issue 4: Inconsistent return types

Cause:

mixing string / dict / int

Fix:

standardized response format

Issue 5: Wrong mental model

Cause:

assuming variables store copies

Fix:

Python stores references

6. MENTAL MODELS (VERY IMPORTANT)

Model 1: Reference Model

Bank.accounts → holds references (not copies)

Modifying object = modifying original

Model 2: Layered System

User → Interface (Bank) → Logic (Account) → Data

Model 3: Responsibility

Bank = controller  
Account = logic  
Data = state

Model 4: Abstraction Rule

“Use methods, don’t touch internals”

Model 5: System Thinking

Before:

objects

Now:

system

"""