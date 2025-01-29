import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.pessoa_juridica import PessoaJuridica
from models.pessoa_juridica_model import PessoaJuridicasModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class PessoaJuridicasRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, pessoa_juridica: PessoaJuridica) -> None:
        pessoa_juridica_model = PessoaJuridicasModel()
        pessoa_juridica_dict = pessoa_juridica.model_dump()

        for k in PessoaJuridicasModel.get_normal_fields():
            if (k not in pessoa_juridica_dict):
                continue
            pessoa_juridica_model[k] = pessoa_juridica_dict[k]
        

        for k in PessoaJuridicasModel.sensivity_fields:
            pessoa_juridica_model[k] = SensivityField(fernet=self.fernet, data=pessoa_juridica_dict[k])

        pessoa_juridica_model.password = bcrypt.hashpw(f'{pessoa_juridica.password}'.encode(), bcrypt.gensalt()).decode()

        pessoa_juridica_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[PessoaJuridicasModel]:
        result = PessoaJuridicasModel.objects(email=email)
        return result
    
    def find_by_phone_number(self, phone: str) -> list[PessoaJuridicasModel]:
        result = PessoaJuridicasModel.objects(phone=phone)
        return result
    
    def find_by_id(self, id: str) -> list[PessoaJuridicasModel]:
        result = PessoaJuridicasModel.objects(id=id)
        return result
    
    def find_by_cnpj(self, cnpj: str) -> str:
        result = PessoaJuridicasModel.objects(cnpj=cnpj)
        return result
        
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        PessoaJuridicasModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[PessoaJuridicasModel]:
        result: list[PessoaJuridicasModel] = PessoaJuridicasModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        PessoaJuridicasModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        pessoa_juridica = PessoaJuridicasModel.objects(id=id).first()
        return pessoa_juridica.name
        
    def get_email(self, id: str) -> str:
        pessoa_juridica = PessoaJuridicasModel.objects(id=id).first()
        return pessoa_juridica.email
        
    def get_phone_number(self, id: str) -> str:
        pessoa_juridica = PessoaJuridicasModel.objects(id=id).first()
        return pessoa_juridica.phone_number
        
    def update_name(self, id: str, name: str) -> None:
        PessoaJuridicasModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        PessoaJuridicasModel.objects(id=id).update(set__email = email)
        return None