import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.pessoa_fisica import PessoaFisica
from models.pessoa_fisica_model import PessoaFisicasModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class PessoaFisicasRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, pessoa_fisica: PessoaFisica) -> None:
        pessoa_fisica_model = PessoaFisicasModel()
        pessoa_fisica_dict = pessoa_fisica.model_dump()

        for k in PessoaFisicasModel.get_normal_fields():
            if (k not in pessoa_fisica_dict):
                continue

            pessoa_fisica_model[k] = pessoa_fisica_dict[k]

        for k in PessoaFisicasModel.sensivity_fields:
            print(pessoa_fisica_dict)
            pessoa_fisica_model[k] = SensivityField(fernet=self.fernet, data=pessoa_fisica_dict[k])

        pessoa_fisica_model.password = bcrypt.hashpw(f'{pessoa_fisica.password}'.encode(), bcrypt.gensalt()).decode()

        pessoa_fisica_model.save()


        return None
    
    def find_by_email(self, email: str) -> list[PessoaFisicasModel]:
        result = PessoaFisicasModel.objects(email=email)
        return result
    
    def find_by_phone_number(self, phone_number: str) -> list[PessoaFisicasModel]:
        result = PessoaFisicasModel.objects(phone_number=phone_number)
        return result
    
    def find_by_id(self, id: str) -> list[PessoaFisicasModel]:
        result = PessoaFisicasModel.objects(id=id)
        return result
    
    def find_by_cpf(self, cpf: str) -> str:
        result = PessoaFisicasModel.objects(cpf=cpf)
        return result
        
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        PessoaFisicasModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[PessoaFisicasModel]:
        result: list[PessoaFisicasModel] = PessoaFisicasModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        PessoaFisicasModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        pessoa_fisica = PessoaFisicasModel.objects(id=id).first()
        return pessoa_fisica.name

    def get_email(self, id: str) -> str:
        pessoa_fisica = PessoaFisicasModel.objects(id=id).first()
        return pessoa_fisica.email
        

    def get_plan_id(self, id: str) -> str:
        pessoa_fisica = PessoaFisicasModel.objects(id=id).first()
        return pessoa_fisica.plan_id
        
    def get_phone_number(self, id: str) -> str:
        pessoa_fisica = PessoaFisicasModel.objects(id=id).first()
        return pessoa_fisica.phone_number
        
        
    def update_name(self, id: str, name: str) -> None:
        PessoaFisicasModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        PessoaFisicasModel.objects(id=id).update(set__email = email)
        return None