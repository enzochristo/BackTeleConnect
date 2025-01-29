from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import FastAPI, Request, Response, HTTPException
from use_cases.pessoa_fisica.auth.login.login_dto import LoginDTO
from entities.pessoa_fisica import PessoaFisica
import jwt
import os

class LoginUseCase:
    pessoa_fisica_repository: PessoaFisicasRepository

    def __init__(self, pessoa_fisica_repository: PessoaFisicasRepository):
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        pessoa_fisica = None

        # Tenta encontrar o cliente pelo email se fornecido
        if login_dto.email:
            pessoa_fisica = self.pessoa_fisica_repository.find_by_email(email=login_dto.email).first()
        
        # Se nenhum cliente foi encontrado pelo email, tenta pelo telefone
        if not pessoa_fisica and login_dto.phone_number:
            pessoa_fisica = self.pessoa_fisica_repository.find_by_phone_number(phone_number=login_dto.phone_number).first()

        # Se nenhum cliente foi encontrado ainda, retorna erro
        if not pessoa_fisica:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado com as credenciais fornecidas"}

        # Verifica a senha
        if not pessoa_fisica.check_password_matches(login_dto.password):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        # Gera o token JWT
        token = jwt.encode({"id": str(pessoa_fisica.id)}, os.getenv("PF_JWT_SECRET"))

        # Define o cookie de autenticação
        response.set_cookie(key="pessoa_fisica_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}
