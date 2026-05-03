from app.services.bank_service import Bank

bank_instance = Bank()

def get_bank():
    return bank_instance