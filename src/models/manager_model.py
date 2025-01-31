from mongoengine import *
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet
from models.fields.sensivity_field import SensivityField

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ManagersModel(Document):
    # Lista de campos sensíveis para controle interno
    sensivity_fields = [
    ]

    # Campos do modelo
    name = StringField(required=True)
    cpf = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    comp_password = StringField(required=True)

    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)


    def get_normal_fields():
        return [i for i in ManagersModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in ManagersModel.sensivity_fields]
    
    

    def check_password_matches(self, password: str) -> bool:
        """Verifica se a senha fornecida coincide com a senha criptografada."""
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))
    
    def check_comp_password_matches(hashed_comp_password, plain_comp_password):
        return bcrypt.checkpw(plain_comp_password.encode('utf-8'), hashed_comp_password.encode('utf-8'))
    


   
