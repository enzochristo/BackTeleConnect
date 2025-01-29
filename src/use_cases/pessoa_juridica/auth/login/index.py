from use_cases.pessoa_juridica.auth.login.login_use_case import LoginUseCase
from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from fastapi import FastAPI, Request, Response
from use_cases.pessoa_juridica.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

pessoa_juridica_repository = PessoaJuridicasRepository()
login_use_case = LoginUseCase(pessoa_juridica_repository)

@router.post("/pessoa/juridica/auth/login")
def pessoa_juridica_login(pessoa_juridica_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(pessoa_juridica_login_dto, response, request)