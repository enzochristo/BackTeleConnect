from pydantic import BaseModel, EmailStr

class RegisterManagerDTO(BaseModel):
    name: str
    email: str
    cpf  : str
    password: str
    comp_password: str 
