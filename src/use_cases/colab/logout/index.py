from fastapi import APIRouter, Depends, Response
from use_cases.colab.logout.logout_use_case import LogoutManagerUseCase
from middlewares.validate_manager_auth_token import validate_manager_auth_token



router = APIRouter()

logout_manager_use_case = LogoutManagerUseCase()

@router.post("/manager/logout", dependencies=[Depends(validate_manager_auth_token)])
def logout_manager(response: Response):
    return logout_manager_use_case.execute(response)