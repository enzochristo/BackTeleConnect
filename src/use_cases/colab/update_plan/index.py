from fastapi import APIRouter, Depends, Body
from use_cases.colab.update_plan.update_plan_use_case import UpdatePlanUseCase
from repositories.plan_repository import PlanRepository
from use_cases.colab.update_plan.update_plan_dto import UpdatePlanDTO
from middlewares.validate_manager_auth_token import validate_manager_auth_token

router = APIRouter()

plan_repository = PlanRepository()
update_plan_use_case = UpdatePlanUseCase(plan_repository)

@router.put("/manager/update/{plan_id}", dependencies=[Depends(validate_manager_auth_token)])
def update_plan(plan_id: str, update_plan_dto: UpdatePlanDTO ):
    return update_plan_use_case.execute(plan_id, update_plan_dto)
