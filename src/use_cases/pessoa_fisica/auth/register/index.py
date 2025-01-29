from use_cases.pessoa_fisica.auth.register.register_use_case import RegisterUseCase
from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import FastAPI, Request, Response
from use_cases.pessoa_fisica.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

pessoa_fisica_repository = PessoaFisicasRepository()
pessoa_fisica_register_use_case = RegisterUseCase(pessoa_fisica_repository)

@router.post("/pessoa/fisica/auth/register")
def pessoa_fisica_register(register_dto: RegisterDTO, response: Response, request: Request):
    return pessoa_fisica_register_use_case.execute(register_dto, response, request)
    