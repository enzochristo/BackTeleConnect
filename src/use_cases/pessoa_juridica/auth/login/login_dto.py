from pydantic import BaseModel, validator
from typing import Literal, Optional

class LoginDTO(BaseModel):
    cnpj: str
    password: str

    