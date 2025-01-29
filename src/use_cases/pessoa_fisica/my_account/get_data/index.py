from use_cases.pessoa_fisica.my_account.get_data.get_data_use_case import getPessoaFisicaData
from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from middlewares.validate_pessoa_fisica_auth_token import validade_pessoa_fisica_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

pessoa_fisica_repository = PessoaFisicasRepository()

get_data_use_case = getPessoaFisicaData(pessoa_fisica_repository)

@router.get("/pessoa/fisica/data", dependencies=[Depends(validade_pessoa_fisica_auth_token)])
def get_pessoa_fisica_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)