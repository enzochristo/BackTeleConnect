from repositories.purchased_plan_repository import PurchasedPlansRepository
from use_cases.pessoa_juridica.purchased_plan_use_case.purchased_plan_dto import PurchasedPlanDTO
from entities.purchased_plan import PurchasedPlan
from fastapi import Response, Request
from datetime import datetime

class PurchasedPlanUseCase:
    def __init__(self, purchased_plan_repository: PurchasedPlansRepository):
        self.purchased_plan_repository = purchased_plan_repository

    def execute(self, purchased_plan_dto: PurchasedPlanDTO, response: Response, request: Request):
        required_fields = [
        purchased_plan_dto.plan_type,
        purchased_plan_dto.final_price,
        purchased_plan_dto.cep,
        purchased_plan_dto.rua,
        purchased_plan_dto.cidade,
        purchased_plan_dto.numero,
        purchased_plan_dto.estado
        ]

        if any(value is None for value in required_fields):
            response.status_code = 400
            return {"status": "error", "message": "Missing required fields"}

        now = datetime.now()
        customer_id = request.state.auth_payload["pessoa_juridica_id"]
        customer_id = request.state.auth_payload.get("pessoa_juridica_id")

        if not customer_id:
            response.status_code = 400
            return {"status": "error", "message": "Customer ID (pessoa_juridica_id) is missing"}


        print("Received DTO:", purchased_plan_dto)

        # Verifica se todos os valores esperados estão presentes
        print("Plan Type:", purchased_plan_dto.plan_type)
        print("Speed:", purchased_plan_dto.speed)
        print("Final Price:", purchased_plan_dto.final_price)
        print("CEP:", purchased_plan_dto.cep)
        print("Rua:", purchased_plan_dto.rua)
        print("Cidade:", purchased_plan_dto.cidade)
        print("Numero:", purchased_plan_dto.numero)
        print("Estado:", purchased_plan_dto.estado)


        purchased_plan = PurchasedPlan(
            customer_id=customer_id,
            plan_type=purchased_plan_dto.plan_type,
            speed=purchased_plan_dto.speed,
            final_price=purchased_plan_dto.final_price,
            cep=purchased_plan_dto.cep,
            rua=purchased_plan_dto.rua,
            cidade=purchased_plan_dto.cidade,
            numero=purchased_plan_dto.numero,
            estado=purchased_plan_dto.estado,
            created_at=now
        )
        print("Purchased Plan Data:", vars(purchased_plan))


        self.purchased_plan_repository.save(purchased_plan)
        response.status_code = 201
        return {"status": "success", "message": "Plan registered successfully for PJ"}
