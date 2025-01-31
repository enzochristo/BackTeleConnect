from repositories.plan_repository import PlanRepository

class GetAllPlansUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self):
        plans = self.plan_repository.list_all_plans()
        return plans
