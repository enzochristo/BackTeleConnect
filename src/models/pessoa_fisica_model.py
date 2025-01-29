from mongoengine import *
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet
from datetime import timedelta

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PessoaFisicasModel(Document):
    sensivity_fields = [
        
    ]

    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    cpf = StringField(required=True)  # Certifique-se de que 'required=True' se necessário
    phone_number = StringField(required=True)
    last_payment_date = DateTimeField()
    billing_cycle = IntField(default=30)
    next_payment_date = DateTimeField()
    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)


    def get_normal_fields():
        return [i for i in PessoaFisicasModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in PessoaFisicasModel.sensivity_fields]
    
    def check_password_matches(self, password: str) -> bool:
        """Verifica se a senha fornecida coincide com a senha criptografada."""
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def calculate_next_payment_date(self):
        """Calcula a próxima data de pagamento baseada no último pagamento e no ciclo de cobrança."""
        if not self.last_payment_date:
            return None
        return self.last_payment_date + timedelta(days=self.billing_cycle)