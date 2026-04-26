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
def deposi(account_id : str, amount : float):
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