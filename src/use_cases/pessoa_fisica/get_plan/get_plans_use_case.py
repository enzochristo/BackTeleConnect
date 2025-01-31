from fastapi import Request
from repositories.purchased_plan_repository import PurchasedPlansRepository

class GetPlansUseCase:
    def __init__(self, purchased_plans_repository: PurchasedPlansRepository):
        self.purchased_plans_repository = purchased_plans_repository

    def execute(self, request: Request):
        """ Pega o customer_id autenticado e retorna os planos associados. """
        customer_id = request.state.auth_payload.get("pessoa_fisica_id")  # Pegando ID do usuário autenticado

        if not customer_id:
            return {"status": "error", "message": "Usuário não autenticado"}

        plans = self.purchased_plans_repository.get_plans_by_customer_id(customer_id)

        return plans
