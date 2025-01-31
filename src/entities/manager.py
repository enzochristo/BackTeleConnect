import dotenv
from pydantic import BaseModel
dotenv.load_dotenv()

class Manager(BaseModel):
    _id: str
    name: str
    cpf: str
    email: str
    password: str
    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0
    comp_password: str
