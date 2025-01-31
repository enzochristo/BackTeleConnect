from use_cases.colab.headbar.get_manager_name_use_case import getManagerName
from repositories.manager_repository import ManagersRepository
from middlewares.validate_manager_auth_token import validate_manager_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

manager_repository = ManagersRepository()

get_manager_name_use_case = getManagerName(manager_repository)

@router.get("/manager/headbar", dependencies=[Depends(validate_manager_auth_token)])
def get_manager_name(response: Response, request:Request):
    return get_manager_name_use_case.execute(response,request)