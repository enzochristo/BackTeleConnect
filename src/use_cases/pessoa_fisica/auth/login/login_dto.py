from pydantic import BaseModel, validator
from typing import Literal, Optional

class LoginDTO(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None
    password: str

    