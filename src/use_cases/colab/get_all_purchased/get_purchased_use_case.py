from repositories.purchased_plan_repository import PurchasedPlansRepository

class GetPurchasedPlansUseCase:
    def __init__(self, purchased_plan_repository: PurchasedPlansRepository):
        self.purchased_plan_repository = purchased_plan_repository

    def execute(self):
        plans = self.purchased_plan_repository.get_all_purchased_plans()
        if not plans:
            return {"status": "error", "message": "No purchased plans found"}

        return {"status": "success", "data": plans}
