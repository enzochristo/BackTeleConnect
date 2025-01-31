from use_cases.colab.my_account.get_data.get_data_use_case import getManagerData
from repositories.manager_repository import ManagersRepository
from middlewares.validate_manager_auth_token import validate_manager_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

manager_repository = ManagersRepository()

get_data_use_case = getManagerData(manager_repository)

@router.get("/manager/data", dependencies=[Depends(validate_manager_auth_token)])
def get_manager_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)