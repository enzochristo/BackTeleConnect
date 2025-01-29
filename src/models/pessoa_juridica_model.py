from mongoengine import *
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet
from datetime import timedelta

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PessoaJuridicasModel(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    cnpj = StringField(required=True, unique=True)
    phone_number = StringField(required=True)
    last_payment_date = DateTimeField()
    billing_cycle = IntField(default=30)
    next_payment_date = DateTimeField()
    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    # Definindo campos sensíveis específicos para pessoa jurídica
    sensivity_fields = [
    ]

    def get_normal_fields():
        return [i for i in PessoaJuridicasModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in PessoaJuridicasModel.sensivity_fields]

    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")

        encrypted_value = getattr(self, field, None)
        return fernet.decrypt(encrypted_value.encode()).decode() if encrypted_value else None

    def check_password_matches(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))
    
    def calculate_next_payment_date(self):
        if not self.last_payment_date:
            return None
        return self.last_payment_date + timedelta(days=self.billing_cycle)
