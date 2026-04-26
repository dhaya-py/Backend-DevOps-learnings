# 🚀 Backend & DevOps Learnings - OOP Fundamentals

Welcome to my learning repository! This project serves as a structured log of my journey through Backend Development, specifically focusing on Object-Oriented Programming (OOP) fundamentals, system architecture, and building resilient code.

Here, I document the Python Banking System I've built, the code architectures I've designed, the issues I've encountered, and the mental models I've developed along the way.

---

## 📑 Table of Contents
1. [What I Have Done So Far](#-what-i-have-done-so-far)
2. [System Workflow & Steps](#-system-workflow--steps)
3. [Key Notes & Definitions](#-key-notes--definitions)
4. [Issues Faced & How They Were Handled](#-issues-faced--how-they-were-handled)
5. [Mental Models Developed](#-mental-models-developed)

---

## 🛠️ What I Have Done So Far

### Object-Oriented Programming (Python)
- **Banking System Simulation**: Built a robust banking system utilizing core OOP principles.
- **Class Hierarchy**: Created `BankAccount`, `SavingsAccount`, and `CurrentAccount` classes to handle specific banking behaviors (like calculating interest and managing overdraft limits).
- **Interface Layer**: Implemented `interface_layer.py` (`Bank` class) to handle abstractions, restrict direct access to account objects, and provide a professional-grade facade for interacting with the system.
- **Transaction History**: Engineered a dictionary-based transaction storage system with dynamic metadata generation (timestamps and transaction IDs).
- **Rollback Mechanisms**: Built a `transfer` method that can safely move funds between objects and trigger a rollback if any step fails, preventing data corruption.

---

## 🔄 System Workflow & Steps

### 1. Account Creation
- **User** -> `Bank.create_account()`
- The `Bank` interface instantiates a specific object (`SavingsAccount` or `CurrentAccount`).
- The `Bank` stores the object in an internal dictionary.
- The `Bank` returns a newly generated `account_id` (e.g., "A1") to the user.

### 2. Deposit / Withdraw
- **User** -> `Bank.deposit(account_id)`
- The `Bank` finds the account reference using the ID.
- The `Bank` delegates the task by calling the internal `acc.deposit()` method.
- The `Bank` standardizes the response to a dictionary and returns the result.

### 3. Transfer Workflow (Rollback Mechanism)
1. **Validation**: Check if the target account is the same as the source account and verify both exist.
2. **Withdrawal**: Deduct the amount from the sender's account.
3. **Deposit**: Add the amount to the receiver's account.
4. **Rollback**: If the deposit into the target account fails for any reason, it automatically calls `deposit` on the sender's account to refund the deducted amount back, ensuring no money is lost during an unexpected failure.

---

## 📝 Key Notes & Definitions

### Core OOP Concepts
- **Classes & Objects**: A class is a blueprint (e.g., `BankAccount`), while an object is a specific, stateful instance of it.
- **Encapsulation**: Bundling data and restricting direct access using private (`__overdraft`) and protected (`_balance`) modifiers to protect data integrity. **Rule: Expose methods, hide data.**
- **Inheritance**: Reusing and extending behavior. `SavingsAccount` and `CurrentAccount` inherit core logic from `BankAccount`.
- **Polymorphism**: The same method behaving differently based on the object. For example, `withdraw()` behaves differently for a `CurrentAccount` (checks overdraft) compared to a `SavingsAccount`.
- **Abstraction**: Hiding internal complexity. The user interacts via `acc.deposit()` rather than manually updating `acc._balance`.

### Interface Layers (Facade Pattern)
- **Definition**: The interface layer dictates how the outside world interacts with your system.
- **Rule**: Users should *never* interact with account objects directly. They talk to the `Bank`, and the `Bank` talks to the `Account`.

---

## 🚨 Issues Faced & How They Were Handled

1. **Issue:** `AttributeError: 'tuple' object has no attribute 'deposit'`
   - *Cause:* I was mixing internal object handling with external responses. `get_account()` was returning a tuple `(True, data)` instead of the raw account object.
   - *Handling:* I clearly separated concerns: internal methods return **objects**, while external interface methods return **standardized dictionaries**.

2. **Issue:** Breaking Abstraction
   - *Cause:* Accessing `__transactions` or `_balance` directly from outside the class.
   - *Handling:* Enforced the use of public methods like `get_balance()` and `get_transaction()` to fetch data without exposing mutable internals.

3. **Issue:** Inconsistent Return Types
   - *Cause:* Mixing return types (e.g., returning strings sometimes, ints others, dicts others).
   - *Handling:* Standardized the API response format across the entire Interface Layer: `(True, {"message": "...", "data": ...})` or `(False, {"message": "...", "data": None})`.

---

## 🧠 Mental Models Developed

1. **The Reference Model**
   - *Model:* Python stores references, not copies. The `Bank.accounts` dictionary holds a *reference* to the account object. Modifying the object modifies the original data.

2. **The Layered System Model**
   - *Model:* Systems should be structured sequentially: `User -> Interface (Bank) -> Logic (Account) -> Data`. Never skip a layer.

3. **Separation of Responsibilities**
   - *Model:* 
     - **Bank** = The Controller (handles routing and validation)
     - **Account** = The Logic (handles the business rules like overdrafts)
     - **Variables** = The State (holds the current truth)

4. **The Abstraction Rule**
   - *Model:* "Use methods, don't touch internals." Always write code against the interface, not the concrete implementation.


---

## API Layer Integration (FastAPI)

### What I Have Built So Far
- **End-to-End API Backend**: Successfully connected FastAPI to the Interface Layer (Bank).
- **Exposed Endpoints**: Built functioning endpoints handling HTTP requests for account creation, deposits, withdrawals, transfers, and statements.

### System Workflow & Request Flow
- **The Core Backend Request Flow**: Client -> HTTP request -> Uvicorn -> FastAPI -> Interface Layer (Bank) -> Response.
- **FastAPI Controller**: Extracts inputs automatically from the request and injects values into the mapped function.
- **Routing**: Maps a URL and HTTP method directly to a Python function.

### Key Notes & Definitions
- **FastAPI Fundamentals**: Initializes the API application, serving as the central controller. Exposes Python functions over HTTP.
- **Data Safety Rule**: 
  - Internal: Use strict objects or None.
  - External: Use structured responses (JSON/Dictionaries).

### Issues Faced & How They Were Handled
1. **Issue:** AttributeError: 'str' object has no attribute 'deposit'
   - Cause: get_account() was returning a string ("Account not found") when an account didn't exist. Later, to_acc.deposit() crashed because it tried to call .deposit() on that string.
   - Handling: Changed internal logic to return predictable types (object or None). Validated the object via "if acc is None:" before calling methods on it.

2. **Issue:** SyntaxError: unterminated string literal
   - Cause: A malformed string declaration.
   - Handling: Fixed the syntax error, reinforcing that small syntactical mistakes can crash the entire backend server.

### Mental Models Developed
1. **The Layered Backend System**
   - Model: A robust system separates concerns across layers: API Layer -> Service Layer -> Business Logic -> Data.
2. **Control Flow Isolation**
   - Model: FastAPI's role is strictly routing requests, not handling business logic.
3. **Data Safety Boundaries**
   - Model: Internal communications should use objects or None, while external API responses must use structured data.
4. **Error Anticipation**
   - Model: Never assume a successful operation. Always validate objects before utilizing them.

### Current Skill Assessment & Focus Areas
- Strong: Python basics, Object-Oriented Programming.
- Clear: Backend request flows, FastAPI fundamentals.
- Emerging: Real-world backend architecture.
- Focus Areas: Proper API structure (files, modules), request validation (Pydantic), proper HTTP status codes, robust error handling, and data persistence (Database).