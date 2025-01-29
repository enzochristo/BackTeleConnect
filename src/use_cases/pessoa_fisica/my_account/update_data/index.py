from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_pessoa_fisica_auth_token import validade_pessoa_fisica_auth_token

router = APIRouter()

pessoa_fisica_repository = PessoaFisicasRepository()
update_data_use_case = UpdateDataUseCase(pessoa_fisica_repository)

@router.put("/pessoa/fisica/update/data", dependencies=[Depends(validade_pessoa_fisica_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)
