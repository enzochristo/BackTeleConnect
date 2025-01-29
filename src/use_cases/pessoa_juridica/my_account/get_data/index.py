from use_cases.pessoa_juridica.my_account.get_data.get_data_use_case import getPessoaJuridicaData
from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from middlewares.validate_pessoa_juridica_auth_token import validate_pessoa_juridica_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

pessoa_juridica_repository = PessoaJuridicasRepository()

get_data_use_case = getPessoaJuridicaData(pessoa_juridica_repository)

@router.get("/pessoa/juridica/data", dependencies=[Depends(validate_pessoa_juridica_auth_token)])
def get_pessoa_juridica_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)