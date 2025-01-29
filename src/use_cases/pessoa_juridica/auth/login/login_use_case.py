from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from fastapi import FastAPI, Request, Response, HTTPException
from use_cases.pessoa_juridica.auth.login.login_dto import LoginDTO
from entities.pessoa_juridica import PessoaJuridica
import jwt
import os

class LoginUseCase:
    pessoa_juridica_repository: PessoaJuridicasRepository

    def __init__(self, pessoa_juridica_repository: PessoaJuridicasRepository):
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):

        pessoa_juridica = self.pessoa_juridica_repository.find_by_cnpj(cnpj=login_dto.cnpj).first()

        # Se nenhum cliente foi encontrado ainda, retorna erro
        if not pessoa_juridica:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado com as credenciais fornecidas"}

        # Verifica a senha
        if not pessoa_juridica.check_password_matches(login_dto.password):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        # Gera o token JWT
        token = jwt.encode({"id": str(pessoa_juridica.id)}, os.getenv("PJ_JWT_SECRET"))

        # Define o cookie de autenticação
        response.set_cookie(key="pessoa_juridica_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}
