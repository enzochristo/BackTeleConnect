from use_cases.pessoa_juridica.headbar.get_pessoa_juridica_name_use_case import getPessoaJuridicaName
from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from middlewares.validate_pessoa_juridica_auth_token import validate_pessoa_juridica_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

pessoa_juridica_repository = PessoaJuridicasRepository()

get_pessoa_juridica_name_use_case = getPessoaJuridicaName(pessoa_juridica_repository)

@router.get("/pessoa/juridica/headbar", dependencies=[Depends(validate_pessoa_juridica_auth_token)])
def get_pessoa_juridica_name(response: Response, request:Request):
    return get_pessoa_juridica_name_use_case.execute(response,request)