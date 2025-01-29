from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import FastAPI, Request, Response
from use_cases.pessoa_fisica.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.pessoa_fisica.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from fastapi import APIRouter

router = APIRouter()

pessoa_fisica_repository = PessoaFisicasRepository()
reset_pwd_use_case = ResetPwdUseCase(pessoa_fisica_repository)

@router.post("/pessoa/fisica/auth/reset/pwd")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
    