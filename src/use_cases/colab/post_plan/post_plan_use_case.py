from repositories.plan_repository import PlanRepository
from use_cases.colab.post_plan.post_plan_dto import PostPlanDTO
from entities.plan import Plan
from fastapi import Response
from datetime import datetime

class PostPlanUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self, post_plan_dto: PostPlanDTO, response: Response):
        if not post_plan_dto.name or not post_plan_dto.tipo or not post_plan_dto.price:
            response.status_code = 400
            return {"status": "error", "message": "Missing required fields"}

        now = datetime.now()
        plan = Plan(
            name=post_plan_dto.name,
            tipo=post_plan_dto.tipo,
            vel_max=post_plan_dto.vel_max,
            vel_min=post_plan_dto.vel_min,
            price=post_plan_dto.price,
            benefits=post_plan_dto.benefits,
            created_at=now,
            updated_at= None
        )
        self.plan_repository.save(plan)
        response.status_code = 201
        return {"status": "success", "message": "Plan created successfully"}
