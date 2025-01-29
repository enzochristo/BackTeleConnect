from use_cases.pessoa_fisica.headbar.get_pessoa_fisica_name_use_case import getPessoaFisicaName
from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from middlewares.validate_pessoa_fisica_auth_token import validade_pessoa_fisica_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

pessoa_fisica_repository = PessoaFisicasRepository()

get_pessoa_fisica_name_use_case = getPessoaFisicaName(pessoa_fisica_repository)

@router.get("/pessoa/fisica/headbar", dependencies=[Depends(validade_pessoa_fisica_auth_token)])
def get_pessoa_fisica_name(response: Response, request:Request):
    return get_pessoa_fisica_name_use_case.execute(response,request)