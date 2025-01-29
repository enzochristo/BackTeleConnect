from pydantic import BaseModel, ConfigDict
from typing import Literal


class RegisterDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    phone_number: str
    cnpj: str
    email: str
    password: str