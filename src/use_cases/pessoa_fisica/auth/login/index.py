from use_cases.pessoa_fisica.auth.login.login_use_case import LoginUseCase
from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import FastAPI, Request, Response
from use_cases.pessoa_fisica.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

pessoafisica_repository = PessoaFisicasRepository()
login_use_case = LoginUseCase(pessoafisica_repository)

@router.post("/pessoa/fisica/auth/login")
def pessoa_fisica_login(pessoafisica_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(pessoafisica_login_dto, response, request)