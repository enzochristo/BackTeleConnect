from pydantic import BaseModel, ConfigDict
from typing import Literal


class RegisterDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    phone_number: str
    cpf: str
    email: str
    password: str