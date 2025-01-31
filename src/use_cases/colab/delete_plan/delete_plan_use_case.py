from repositories.plan_repository import PlanRepository
from fastapi import HTTPException

class DeletePlanUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self, plan_id: str):
        self.plan_repository.delete_plan(plan_id)
        return {"status": "success", "message": "Plano deletado com sucesso."}
