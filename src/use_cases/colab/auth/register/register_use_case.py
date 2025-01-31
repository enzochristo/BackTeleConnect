from repositories.manager_repository import ManagersRepository
from use_cases.colab.auth.register.register_dto import RegisterManagerDTO
from fastapi import Request, Response
from entities.manager import Manager

class RegisterUseCase:
    manager_repository = ManagersRepository

    def __init__(self, manager_repository: ManagersRepository):
        self.manager_repository = manager_repository

    def execute(self, register_dto: RegisterManagerDTO, response: Response, request: Request):
        # Senha fixa da companhia
        COMPANY_PASSWORD = "senhamanager123"

        # 🔹 1️⃣ Verifica se todos os campos foram preenchidos
        if not register_dto.email or not register_dto.password or not register_dto.cpf or not register_dto.name or not register_dto.comp_password:
            response.status_code = 406
            return {"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        # 🔹 2️⃣ Verifica se a senha da companhia está correta
        if register_dto.comp_password != COMPANY_PASSWORD:
            response.status_code = 403
            return {"status": "error", "message": "Invalid company password"}

        # 🔹 3️⃣ Verifica se o manager já está registrado
        if self.manager_repository.find_by_email(register_dto.email):
            response.status_code = 400
            return {"status": "error", "message": "Manager already registered"}

        # 🔹 4️⃣ Cria o objeto Manager e salva no banco
        manager = Manager(**register_dto.model_dump())
        self.manager_repository.save(manager)

        response.status_code = 201
        return {"status": "success", "message": "Cadastro do manager realizado com sucesso"}
