from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from use_cases.colab.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.colab.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from fastapi import APIRouter

router = APIRouter()

manager_repository = ManagersRepository()
reset_pwd_use_case = ResetPwdUseCase(manager_repository)

@router.post("/manager/auth/reset/pwd")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
    