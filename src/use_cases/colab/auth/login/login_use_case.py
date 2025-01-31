from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response, HTTPException
from use_cases.colab.auth.login.login_dto import LoginDTO
from entities.manager import Manager
import jwt
import os

class LoginUseCase:
    manager_repository: ManagersRepository

    def __init__(self, manager_repository: ManagersRepository):
        self.manager_repository = manager_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        manager = self.manager_repository.find_by_email(email=login_dto.email).first()
        
        # Se nenhum cliente foi encontrado ainda, retorna erro
        if not manager:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado com as credenciais fornecidas"}

        # Verifica a senha
        if not manager.check_password_matches(login_dto.password):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}
    
        # Gera o token JWT
        token = jwt.encode({"id": str(manager.id)}, os.getenv("MANAGER_JWT_SECRET"))

        # Define o cookie de autenticação
        response.set_cookie(key="manager_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}
