
from fastapi import HTTPException

# HELPER FUNCTION FOR ERROR HANDLING

def handle_error(result):
  error = result["error"]

  if error == "ACCOUNT_NOT_FOUND":
    raise HTTPException(status_code=404, detail=result["error"])

  if error == "INVALID_ACCOUNT_TYPE":
    raise HTTPException(status_code=400, detail=result["error"])

  if error == "INSUFFICIENT_BALANCE":
    raise HTTPException(status_code=400, detail=result["error"])

  if error == "INVALID_AMOUNT":
    raise HTTPException(status_code=400, detail=result["error"])

  if error == "FROM_ACCOUNT_NOT_FOUND":
    raise HTTPException(status_code=404, detail=result["error"])

  if error == "TO_ACCOUNT_NOT_FOUND":
    raise HTTPException(status_code=404, detail=result["error"])

  raise HTTPException(status_code=500, detail="Internal Server Error")