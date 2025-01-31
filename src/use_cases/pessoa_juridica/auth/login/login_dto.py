from pydantic import BaseModel, validator
from typing import Literal, Optional

class LoginDTO(BaseModel):
    email: str
    password: str

    