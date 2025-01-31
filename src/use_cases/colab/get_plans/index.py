from fastapi import APIRouter, Depends
from use_cases.colab.get_plans.get_plan_use_case import GetAllPlansUseCase
from repositories.plan_repository import PlanRepository
from middlewares.validate_manager_auth_token import validate_manager_auth_token

router = APIRouter()

plan_repository = PlanRepository()
get_all_plans_use_case = GetAllPlansUseCase(plan_repository)

@router.get("/manager/get/all/plans", dependencies=[Depends(validate_manager_auth_token)])
def get_all_plans():
    return get_all_plans_use_case.execute()
