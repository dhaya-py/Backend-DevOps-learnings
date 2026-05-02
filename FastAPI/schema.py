from pydantic import BaseModel

class CreateAccount(BaseModel):
    name : str
    balance : float
    acc_type : str

class Deposit(BaseModel):
    account_id : str
    amount : float

class Withdraw(BaseModel):
    account_id : str
    amount : float

class Transfer(BaseModel):
    from_acc_id : str
    to_acc_id : str
    amount : float

# class GetAccountInfo(BaseModel):
#     account_id : str

# class GetBalance(BaseModel):
#     account_id : str

# class Statement(BaseModel):
#     account_id : str