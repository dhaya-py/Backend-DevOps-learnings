# Backend Engineering Learning Journey — OOP to FastAPI

## Overview

This document tracks the complete learning journey from Python OOP fundamentals to building a structured FastAPI backend system.

The journey focused on:
- Understanding concepts deeply instead of copy-pasting
- Debugging and fixing real errors
- Building systems step-by-step
- Developing backend engineering mental models
- Moving from scripts → architecture thinking

---

# Phase 1 — Python OOP Foundations

---

## 1. Classes and Objects

### Concepts Learned

### Class
A class is a blueprint/template.

Example:
```python
class BankAccount:
```

It defines:
- attributes
- methods
- behavior

---

### Object
An object is a real instance created from a class.

Example:
```python
user = BankAccount("Dhaya", 5000)
```

Each object has its own:
- data
- state
- behavior

---

### self Keyword

`self` refers to the current object.

Example:
```python
self.balance
```

Means:
> balance belonging to THIS object

---

## Initial Banking System Built

### Features Implemented
- account creation
- deposit
- withdraw
- check balance
- menu-driven loop
- input handling

---

# Phase 2 — Debugging Fundamentals

---

## Problem Faced — AttributeError

### Error
```python
AttributeError: 'BankAccount' object has no attribute 'amount'
```

### Root Cause
Used:
```python
self.amount
```

Instead of:
```python
amount
```

---

## Key Learning

### Important Difference

```python
self.amount
```
Means:
> object attribute

---

```python
amount
```
Means:
> local function parameter

---

## Debugging Breakthrough

Developed ability to:
- read traceback
- locate exact line
- identify incorrect attribute access
- fix logic independently

This was the first major debugging breakthrough.

---

# Phase 3 — Data Validation and State Management

---

## Features Added

### Validation
Implemented:
- negative deposit prevention
- over-withdraw prevention

### Logic
```python
if amount <= 0:
```

and

```python
if amount > balance:
```

---

## Key Learning

Backend systems must:
- validate inputs
- protect internal state
- prevent invalid operations

---

# Phase 4 — Transaction History System

---

## Features Added

- transaction storage
- transaction logs
- timestamps
- latest transactions

---

## Data Structures Used

### List
```python
self.transactions = []
```

### Dictionary
```python
transaction = {
    "id": "T1",
    "type": "Deposited",
    "amount": 5000
}
```

---

## Key Learning

### Dynamic Record Keeping

Objects can maintain their own internal data history.

Each account object maintained:
- balance
- transactions
- state changes

---

# Phase 5 — Encapsulation

---

## Concepts Learned

### Private Variables

```python
self.__balance
self.__transactions
```

---

## Meaning

Private variables should not be accessed directly outside the class.

Instead:
- controlled through methods
- protects internal state

---

## Methods Added

```python
get_balance()
transaction_history()
```

---

## Key Learning

### Encapsulation

Encapsulation means:
> hiding internal data and controlling access through methods

---

## Important Realization

Changed from:
```python
user.balance
```

To:
```python
user.get_balance()
```

This was the first exposure to:
- controlled access
- safe design
- API-style interaction

---

# Phase 6 — Inheritance

---

## Concepts Learned

### Parent Class
```python
class BankAccount:
```

### Child Classes
```python
class SavingsAccount(BankAccount)
class CurrentAccount(BankAccount)
```

---

## Features Added

### Savings Account
- interest logic

### Current Account
- overdraft support

---

## super() Understanding

```python
super().__init__(name, balance)
```

Used to:
- reuse parent logic
- avoid duplication
- initialize inherited data

---

## Key Learning

Inheritance allows:
- code reuse
- extension of behavior
- specialization of classes

---

# Phase 7 — Polymorphism

---

## Core Understanding

### Same Method
Different Behavior

---

## Example

Both classes had:
```python
withdraw()
```

But:

### SavingsAccount
Normal withdrawal

### CurrentAccount
Overdraft withdrawal

---

## Key Learning

Polymorphism means:
> same interface, different implementation

---

## Important Mental Model

Python checks:
1. current class
2. parent class
3. inheritance chain

This clarified method resolution behavior.

---

# Phase 8 — Access Modifiers

---

## Concepts Learned

### Public
```python
self.name
```

### Protected
```python
self._balance
```

### Private
```python
self.__balance
```

---

## Key Learning

### Protected
Used for:
- inheritance access
- internal framework usage

### Private
Used for:
- strict hiding
- preventing direct access

---

# Phase 9 — Composition

---

## Concepts Learned

Objects can contain/manage other objects.

---

## Bank Class Created

```python
class Bank:
```

The Bank object managed:
- multiple accounts
- account creation
- account lookup
- transactions

---

## Major Breakthrough

Understood:

```text
Bank HAS accounts
```

This was the first architecture-level understanding.

---

# Phase 10 — Abstraction

---

## Initial Confusion

Initially abstraction was misunderstood because of:
- abstractmethod memories
- theory confusion
- decorator confusion

---

## Actual Understanding Achieved

### Abstraction Means

Expose:
- WHAT system does

Hide:
- HOW internally it works

---

## Example

```python
acc1.transfer(acc2, 5000)
```

User only sees:
- transfer action

Hidden internally:
- withdraw
- validation
- deposit
- rollback
- transaction updates

---

## Key Mental Model

### User Perspective
Simple interface

### Internal Perspective
Complex workflow

---

# Phase 11 — Interface Layer

---

## Concepts Learned

Created a centralized Bank interface layer.

---

## Responsibilities

Bank class became:
- controller
- service layer
- operation manager

---

## Major Architectural Shift

Before:
```python
account.deposit()
```

After:
```python
bank.deposit(account_id, amount)
```

---

## Important Realization

Users should NOT directly control internal objects.

Instead:
- system exposes clean operations
- system controls flow

---

## Backend Architecture Mental Model

```text
User → Interface Layer → Business Logic → Data
```

---

# Phase 12 — Internal vs External Logic

---

## Major Bug Faced

### Problem
`get_account()` returned strings instead of objects.

Example:
```python
"Account not found"
```

---

## Result

Attribute errors:
```python
' str ' object has no attribute 'deposit'
```

---

## Root Cause

Internal logic expected:
```python
BankAccount object
```

But received:
```python
string
```

---

## Fix

Changed internal behavior:

### Internal Layer
Returns:
```python
object or None
```

### API Layer
Converts errors to messages.

---

## Key Learning

### Internal systems should use:
- objects
- None
- structured states

NOT:
- user messages

---

# Phase 13 — FastAPI Introduction

---

## Concepts Learned

### FastAPI App

```python
app = FastAPI()
```

Acts as:
- web application
- route manager
- request handler

---

## Routes

```python
@app.get("/")
```

Means:
- HTTP GET
- specific URL path
- mapped Python function

---

## HTTP Understanding

Learned:
- GET
- POST
- request
- response
- endpoint
- URL
- query params

---

## Request Flow Understanding

```text
Client → HTTP Request → Uvicorn → FastAPI → Route → Logic → Response
```

---

# Phase 14 — Connecting Bank to FastAPI

---

## Features Built

Created APIs for:
- create account
- deposit
- withdraw
- transfer
- statement
- get balance

---

## Major Breakthrough

Connected:

```text
FastAPI → Interface Layer → OOP System
```

This transformed the project into:
- real backend service

---

# Phase 15 — Pydantic Validation

---

## Concepts Learned

### BaseModel

Used for:
- request validation
- schema enforcement
- typed request bodies

---

## Example

```python
class Deposit(BaseModel):
    account_id: str
    amount: float = Field(gt=0)
```

---

## Validation Improvements

Added:
- Field(gt=0)
- Field(ge=0)
- regex validation
- min_length
- Enum validation

---

## Major Shift

Validation moved from:

```text
Business Logic ❌
```

To:

```text
Input Layer ✅
```

---

## Key Learning

### Input Validation
Handled by:
- Pydantic

### Business Rules
Handled by:
- Bank logic

---

# Phase 16 — Structured Error Handling

---

## Evolution of Error Handling

### Stage 1
String-based errors

```python
"Account not found"
```

Fragile and unsafe.

---

### Stage 2
Centralized error handling

```python
handle_error()
```

---

### Stage 3
Structured error codes

```python
{"error": "ACCOUNT_NOT_FOUND"}
```

---

## HTTPException Usage

```python
raise HTTPException(status_code=404)
```

---

## Key Learning

### Internal Layer
Uses:
- error codes

### API Layer
Maps:
- error → HTTP response

---

## Major Mental Model

```text
Error Code → API Mapping → HTTP Response
```

---

# Phase 17 — Project Structure Refactor

---

## Before

Everything inside one file.

---

## After

```text
app/
  api/
  schemas/
  services/
  core/
```

---

## Structure Meaning

### api/
HTTP routes

### schemas/
Pydantic validation

### services/
Business logic

### core/
shared utilities

---

## Major Improvement

Removed:
```python
sys.path.append(...)
```

Replaced with:
```python
from app.schemas.schema import ...
```

---

## Key Learning

Learned:
- Python package structure
- modular design
- scalable organization

---

# Phase 18 — Dependency Injection (DI)

---

## Initial Confusion

Initially DI felt unnecessary because:

```python
bank = Bank()
```

already worked.

---

## Final Understanding

### Dependency
Anything required to work.

In this project:
```text
Bank object
```

---

### Injection
Providing dependency from outside.

---

## Core Definition

Dependency Injection means:
> receive required objects instead of creating them inside.

---

## FastAPI DI

### dependencies.py

```python
bank_instance = Bank()

def get_bank():
    return bank_instance
```

---

## Route Usage

```python
bank: Bank = Depends(get_bank)
```

---

## Internal Flow

```text
Request
→ FastAPI sees Depends()
→ calls dependency function
→ injects Bank object
→ route uses dependency
```

---

## Major Learning

### Loose Coupling
Routes no longer create dependencies.

This improved:
- scalability
- testability
- architecture cleanliness

---

# Major Errors Faced Throughout Journey

---

## 1. AttributeError

### Cause
Wrong object access.

### Fixed By
Understanding:
- objects
- attributes
- inheritance chain

---

## 2. Tuple/Object Confusion

### Cause
Returning inconsistent types.

### Fixed By
Standardizing:
- return structures
- internal object flow

---

## 3. String-Based Internal Logic

### Cause
Using messages for logic.

### Fixed By
Using:
```python
{"error": "CODE"}
```

---

## 4. Dependency Object Call Mistake

### Mistake
```python
bank_instance()
```

### Fixed Understanding
Objects are NOT functions.

---

## 5. Validation Layer Confusion

### Before
Validation inside logic.

### After
Validation inside schema layer.

---

# Biggest Mental Models Developed

---

## 1. Layered Architecture

```text
Client
→ FastAPI
→ Router
→ Service Layer
→ Business Logic
→ Data
```

---

## 2. Responsibility Separation

```text
Validation → Pydantic
Business Rules → Bank
HTTP Handling → FastAPI
```

---

## 3. Internal vs External Communication

### Internal
- objects
- None
- error codes

### External
- JSON
- messages
- HTTP responses

---

## 4. System Thinking

Shifted from:
```text
functions
```

To:
```text
interacting backend layers
```

---

## 5. Backend Engineering Thinking

Understanding that:
- clean flow matters
- structure matters
- consistency matters
- scalability matters

---

# Final Technical Stack Learned So Far

---

## Python
- OOP
- classes
- objects
- inheritance
- polymorphism
- encapsulation
- abstraction
- composition

---

## Backend
- FastAPI
- routing
- request handling
- HTTP methods
- APIs
- layered architecture

---

## Validation
- Pydantic
- BaseModel
- Field
- Enum
- regex validation

---

## Architecture
- interface layer
- service layer
- dependency injection
- modular structure
- error handling

---

# Current Level Assessment

| Area | Level |
|------|------|
| Python Fundamentals | Strong |
| OOP | Strong |
| Debugging | Good |
| FastAPI | Strong |
| Validation | Strong |
| API Design | Good |
| Architecture Thinking | Emerging |
| Backend Engineering | Growing Fast |

---

# Current Backend Architecture

```text
Client
→ FastAPI App
→ Router Layer
→ Dependency Injection
→ Service Layer (Bank)
→ OOP Models
→ Data Storage (memory)
```

---

# Important Outcomes Achieved

- Stopped copy-pasting blindly
- Built APIs independently
- Debugged complex errors independently
- Understood architecture flow
- Developed backend mental models
- Built complete structured backend system
- Learned to think in layers and responsibilities

---

# Next Phase

## Database Integration

Current limitation:
```text
Data stored in memory
```

Next upgrade:
```text
Persistent storage using SQLite/database
```

Future topics:
- SQLAlchemy
- ORM
- database sessions
- persistence
- authentication
- async programming
- testing
- production architecture

---

# Final Realization

The journey shifted from:

```text
Learning syntax
```

to:

```text
Learning how backend systems are designed
```

This was the biggest breakthrough of the entire learning process.

