from use_cases.colab.auth.login.login_use_case import LoginUseCase
from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from use_cases.colab.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

pessoafisica_repository = ManagersRepository()
login_use_case = LoginUseCase(pessoafisica_repository)

@router.post("/manager/auth/login")
def manager_login(pessoafisica_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(pessoafisica_login_dto, response, request)