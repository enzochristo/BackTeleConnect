from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_manager_auth_token import validate_manager_auth_token

router = APIRouter()

manager_repository = ManagersRepository()
update_data_use_case = UpdateDataUseCase(manager_repository)

@router.put("/pessoa/fisica/update/data", dependencies=[Depends(validate_manager_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)
