from fastapi import APIRouter, Request, Depends
from use_cases.pessoa_fisica.get_plan.get_plans_use_case import GetPlansUseCase
from repositories.purchased_plan_repository import PurchasedPlansRepository
from middlewares.validate_pessoa_fisica_auth_token import validate_pessoa_fisica_auth_token

router = APIRouter()

purchased_plans_repository = PurchasedPlansRepository()
get_plans_use_case = GetPlansUseCase(purchased_plans_repository)

@router.get("/pessoa/fisica/myplans", dependencies=[Depends(validate_pessoa_fisica_auth_token)])
def get_my_plans(request: Request):
    return get_plans_use_case.execute(request)
