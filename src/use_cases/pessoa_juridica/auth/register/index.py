from use_cases.pessoa_juridica.auth.register.register_use_case import RegisterUseCase
from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from fastapi import FastAPI, Request, Response
from use_cases.pessoa_juridica.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

pessoa_juridica_repository = PessoaJuridicasRepository()
pessoa_juridica_register_use_case = RegisterUseCase(pessoa_juridica_repository)

@router.post("/pessoa/juridica/auth/register")
def pessoa_juridica_register(register_dto: RegisterDTO, response: Response, request: Request):
    return pessoa_juridica_register_use_case.execute(register_dto, response, request)
    