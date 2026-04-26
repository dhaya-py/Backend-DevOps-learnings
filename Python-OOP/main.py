from fastapi import FastAPI
from interface_layer import Bank

app = FastAPI()
bank = Bank()

@app.get("/")
def home():
    return {"message" : "FastAPI is running!"}


@app.post("/create-account")
def create_account(name : str, balance : float, acc_type : str):
    return bank.create_account(name, balance, acc_type)

@app.get("/get-account-info")
def get_account_info(account_id : str):
    return bank.get_account_info(account_id)

@app.post("/deposit")
def deposit(account_id : str, amount : float):
    return bank.deposit(account_id, amount)

@app.post("/withdraw")
def withdraw(account_id : str, amount : float):
    return bank.withdraw(account_id, amount)

@app.get("/get-balance")
def get_balance(account_id : str):
    return bank.get_balance(account_id)

@app.get("/transfer")
def transfer(from_acc_id : str, to_acc_id : str, amount : float):
    return bank.transfer(from_acc_id, to_acc_id, amount)

@app.get("/statement")
def statement(account_id : str):
    return bank.statement(account_id)


"""
================================================================================
FastAPI Fundamentals & Architecture Notes
================================================================================

1. Core Concepts Learned
- FastAPI Application: Initialized via `app = FastAPI()`, serving as the central 
  controller for routing requests.
- Route Mapping: Using decorators like `@app.get("/path")` to map HTTP methods 
  and URLs directly to Python functions.
- API Layer Integration: Successfully connected the FastAPI layer to the 
  underlying Interface Layer (Bank), acting as a bridge between HTTP requests 
  and the application's business logic.
- Request Flow: Client -> HTTP Request -> Uvicorn -> FastAPI -> Function -> Response.

2. System Architecture & Workflows
- Built a complete backend system with functioning endpoints for account 
  creation, deposits, withdrawals, transfers, and statements.
- End-to-end execution confirmed through system logs, ensuring proper data 
  flow from the client to the underlying data structures.

3. Issues Encountered & Resolutions
- Issue: AttributeError: 'str' object has no attribute 'deposit'.
  Cause: The get_account() method returned a string ("Account not found") on 
  failure, causing subsequent operations expecting an object to crash.
  Resolution: Standardized internal methods to strictly return predictable 
  types (object or None). The calling function now validates via 'if acc is None:'.
  Lesson: Internal logic must rely on predictable data types, not strings used 
  as error signals.

- Issue: SyntaxError: unterminated string literal.
  Cause: A malformed string declaration.
  Lesson: Small syntactical errors can halt the entire application server.

4. Mental Models Developed
- Layered Backend Architecture: A robust system separates concerns across layers 
  (API Layer -> Service Layer -> Business Logic -> Data).
- Control Flow Isolation: FastAPI's role is strictly routing requests, not 
  handling business logic.
- Data Safety Boundaries: Internal communications should use objects or None, 
  while external API responses must use structured data (like JSON or dictionaries).
- Error Anticipation: Never assume a successful operation. Always validate 
  objects before utilizing them.
- System-Level Thinking: Transitioning from viewing the application as a set 
  of functions to a cohesive system of interacting layers.

5. Current Skill Assessment & Focus Areas
- Strong foundation in Python basics and Object-Oriented Programming.
- Clear understanding of backend request flows and FastAPI fundamentals.
- Emerging comprehension of real-world backend architecture.
- Future focus areas include implementing structured API modules, request 
  validation (Pydantic), proper HTTP status codes, robust exception handling, 
  and persistent database integration.
================================================================================
"""