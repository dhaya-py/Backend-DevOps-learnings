
from pydantic import BaseModel, Field
from enum import Enum

class AccountType(str, Enum):
    savings = "savings"
    current = "current"

class CreateAccount(BaseModel):
    name : str = Field(min_length=1, max_length=50)
    balance : float = Field(ge=0)
    acc_type : AccountType

class Deposit(BaseModel):
    account_id : str = Field(pattern=r"^A\d+$") 
    amount : float = Field(gt=0)

class Withdraw(BaseModel):
    account_id : str = Field(pattern=r"^A\d+$")
    amount : float = Field(gt=0)

class Transfer(BaseModel):
    from_acc_id : str = Field(pattern=r"^A\d+$")
    to_acc_id : str = Field(pattern=r"^A\d+$")
    amount : float = Field(gt=0)

# class GetAccountInfo(BaseModel):
#     account_id : str

# class GetBalance(BaseModel):
#     account_id : str

# class Statement(BaseModel):
#     account_id : str