from fastapi import FastAPI, APIRouter, Request, Response, Depends
from use_cases.pessoa_fisica.purchased_plan_use_case.purchased_plan_use_case import PurchasedPlanUseCase
from use_cases.pessoa_fisica.purchased_plan_use_case.purchased_plan_dto import PurchasedPlanDTO
from repositories.purchased_plan_repository import PurchasedPlansRepository
from middlewares.validate_pessoa_fisica_auth_token import validate_pessoa_fisica_auth_token

router = APIRouter()

# Instanciação do repositório e do caso de uso para PF
purchased_plans_repository = PurchasedPlansRepository()
purchased_plan_pf_use_case = PurchasedPlanUseCase(purchased_plans_repository)

@router.post("/pessoa/fisica/new/purchased/plan", dependencies=[Depends(validate_pessoa_fisica_auth_token)])
def new_purchased_plan_pf(purchased_plan_dto: PurchasedPlanDTO, response: Response, request: Request):
    return purchased_plan_pf_use_case.execute(purchased_plan_dto, response, request)
