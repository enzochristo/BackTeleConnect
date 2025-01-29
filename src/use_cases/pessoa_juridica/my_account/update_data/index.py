from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_pessoa_juridica_auth_token import validate_pessoa_juridica_auth_token

router = APIRouter()

pessoa_juridica_repository = PessoaJuridicasRepository()
update_data_use_case = UpdateDataUseCase(pessoa_juridica_repository)

@router.put("/pessoa/juridica/update/data", dependencies=[Depends(validate_pessoa_juridica_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)
