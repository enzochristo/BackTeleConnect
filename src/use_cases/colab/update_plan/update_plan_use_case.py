from repositories.plan_repository import PlanRepository
from use_cases.colab.update_plan.update_plan_dto import UpdatePlanDTO
from fastapi import HTTPException

class UpdatePlanUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self, plan_id: str, update_plan_dto: UpdatePlanDTO):
        # Verifica se o plano existe antes de tentar atualizar
        if not self.plan_repository.get_plan_by_id(plan_id):
            raise HTTPException(status_code=404, detail="Plano não encontrado.")

        # Passa os campos individualmente para o repositório
        updated_plan = self.plan_repository.update_plan(
            plan_id=plan_id,
            price=update_plan_dto.price,
            tipo=update_plan_dto.tipo,
            benefits=update_plan_dto.benefits
        )

        return {
            "status": "success",
            "message": "Plano atualizado com sucesso.",
            "data": updated_plan
        }
