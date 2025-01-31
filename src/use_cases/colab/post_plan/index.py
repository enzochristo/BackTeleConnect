from fastapi import FastAPI, APIRouter, Response, Depends
from use_cases.colab.post_plan.post_plan_use_case import PostPlanUseCase
from use_cases.colab.post_plan.post_plan_dto import PostPlanDTO
from repositories.plan_repository import PlanRepository
from middlewares.validate_manager_auth_token import validate_manager_auth_token

router = APIRouter()

# Instanciação do repositório e do caso de uso
plan_repository = PlanRepository()
post_plan_use_case = PostPlanUseCase(plan_repository)

@router.post("/manager/post/plan", dependencies=[Depends(validate_manager_auth_token)])
def post_plan(post_plan_dto: PostPlanDTO, response: Response):
    return post_plan_use_case.execute(post_plan_dto, response)
