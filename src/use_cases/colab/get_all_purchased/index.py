from use_cases.colab.get_all_purchased.get_purchased_use_case import GetPurchasedPlansUseCase
from repositories.purchased_plan_repository import PurchasedPlansRepository
from fastapi import FastAPI, APIRouter, Response, Depends

from middlewares.validate_manager_auth_token import validate_manager_auth_token

router = APIRouter()

purchased_plan_repository = PurchasedPlansRepository()
get_purchased_plans_use_case = GetPurchasedPlansUseCase(purchased_plan_repository)

@router.get("/manager/get/purchased/plans", dependencies=[Depends(validate_manager_auth_token)])
def get_customer_purchased_plans():
    return get_purchased_plans_use_case.execute()
