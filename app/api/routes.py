
from fastapi import APIRouter, Depends
from app.schemas.schema import CreateAccount, Deposit, Withdraw, Transfer
from app.core.error_handler import handle_error
from app.core.dependencies import get_bank
from app.services.bank_service import Bank

router = APIRouter()

@router.post("/create-account")
def create_account(request : CreateAccount, bank : Bank = Depends(get_bank)):
    status, result =  bank.create_account(request.name, request.balance, request.acc_type)
    if not status:
      handle_error(result)
    return result

@router.get("/get-account-info")
def get_account_info(account_id : str, bank : Bank = Depends(get_bank)):
    status, result = bank.get_account_info(account_id)
    if not status:
      handle_error(result)
    return result

@router.post("/deposit")
def deposit(request : Deposit, bank : Bank = Depends(get_bank)):
    status, result = bank.deposit(request.account_id, request.amount)
    if not status:
      handle_error(result)
    return result

@router.post("/withdraw")
def withdraw(request : Withdraw, bank : Bank = Depends(get_bank)):
    status, result = bank.withdraw(request.account_id, request.amount)
    if not status:
      handle_error(result)
    return result

@router.get("/get-balance")
def get_balance(account_id : str, bank : Bank = Depends(get_bank)):
    status, result = bank.get_balance(account_id)
    if not status:
      handle_error(result)
    return result

@router.post("/transfer")
def transfer(request : Transfer, bank : Bank = Depends(get_bank)):
    status, result = bank.transfer(request.from_acc_id, request.to_acc_id, request.amount)
    if not status:
      handle_error(result)
    return result

@router.get("/statement")
def statement(account_id : str, bank : Bank = Depends(get_bank)):
    status, result = bank.statement(account_id)
    if not status:
      handle_error(result)
    return result
