from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PessoaJuridica(BaseModel):
    _id: str
    name: str
    email: str
    phone_number: str
    password: str
    cnpj: str
    last_payment_date: Optional[datetime] = None
    billing_cycle: int = 30
    next_payment_date: Optional[datetime] = None
    
    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0