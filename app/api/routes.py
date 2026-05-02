
from fastapi import APIRouter
from app.services.bank_service import Bank
from app.schemas.schema import CreateAccount, Deposit, Withdraw, Transfer
from app.core.error_handler import handle_error

router = APIRouter()
bank = Bank()

@router.post("/create-account")
def create_account(request : CreateAccount):
    status, result =  bank.create_account(request.name, request.balance, request.acc_type)
    if not status:
      handle_error(result)
    return result

@router.get("/get-account-info")
def get_account_info(account_id : str):
    status, result = bank.get_account_info(account_id)
    if not status:
      handle_error(result)
    return result

@router.post("/deposit")
def deposit(request : Deposit):
    status, result = bank.deposit(request.account_id, request.amount)
    if not status:
      handle_error(result)
    return result

@router.post("/withdraw")
def withdraw(request : Withdraw):
    status, result = bank.withdraw(request.account_id, request.amount)
    if not status:
      handle_error(result)
    return result

@router.get("/get-balance")
def get_balance(account_id : str):
    status, result = bank.get_balance(account_id)
    if not status:
      handle_error(result)
    return result

@router.post("/transfer")
def transfer(request : Transfer):
    status, result = bank.transfer(request.from_acc_id, request.to_acc_id, request.amount)
    if not status:
      handle_error(result)
    return result

@router.get("/statement")
def statement(account_id : str):
    status, result = bank.statement(account_id)
    if not status:
      handle_error(result)
    return result