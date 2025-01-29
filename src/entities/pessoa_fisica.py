import dotenv
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

dotenv.load_dotenv()

class PessoaFisica(BaseModel):
    _id: str
    name: str
    email: str
    password: str
    cpf: str 
    phone_number: str
    last_payment_date: Optional[datetime] = None
    billing_cycle: int = 30
    next_payment_date: Optional[datetime] = None
    
    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0
