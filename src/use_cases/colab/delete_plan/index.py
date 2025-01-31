from fastapi import APIRouter, Depends
from use_cases.colab.delete_plan.delete_plan_use_case import DeletePlanUseCase
from repositories.plan_repository import PlanRepository
from middlewares.validate_manager_auth_token import validate_manager_auth_token

router = APIRouter()

plan_repository = PlanRepository()
delete_plan_use_case = DeletePlanUseCase(plan_repository)

@router.delete("/manager/delete/plan/{plan_id}", dependencies=[Depends(validate_manager_auth_token)])
def delete_plan(plan_id: str):
    print(plan_id)
    return delete_plan_use_case.execute(plan_id)
