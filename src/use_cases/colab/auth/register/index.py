from fastapi import APIRouter, Request, Response
from use_cases.colab.auth.register.register_use_case import RegisterUseCase
from repositories.manager_repository import ManagersRepository
from use_cases.colab.auth.register.register_dto import RegisterManagerDTO

router = APIRouter()

# Criando instâncias
manager_repository = ManagersRepository()
register_manager_use_case = RegisterUseCase(manager_repository)

@router.post("/manager/auth/register")
def register_manager(register_dto: RegisterManagerDTO, response: Response, request: Request):
    return register_manager_use_case.execute(register_dto, response, request)
