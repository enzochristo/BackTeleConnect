import os
from mongoengine import *
from entities.purchased_plan import PurchasedPlan
from models.purchased_plan_model import PurchasedPlanModel
from cryptography.fernet import Fernet
import json
from typing import List
from bson import ObjectId


class PurchasedPlansRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, purchased_plan: PurchasedPlan) -> None:
        purchased_plan_model = PurchasedPlanModel(
        customer_id=purchased_plan.customer_id,
        plan_type=purchased_plan.plan_type,
        speed=purchased_plan.speed,
        final_price=purchased_plan.final_price,
        cep=purchased_plan.cep,
        rua=purchased_plan.rua,
        cidade=purchased_plan.cidade,
        numero=purchased_plan.numero,
        estado=purchased_plan.estado,
        created_at=purchased_plan.created_at
    )

    #  Print os dados antes de salvar
        print(" Purchased Plan Model before saving:", purchased_plan_model.to_mongo().to_dict())

        purchased_plan_model.save()

    from bson import ObjectId

    def get_plans_by_customer_id(self, customer_id: str) -> dict:
        print(f"🔍 Debug - ID do cliente recebido como string: {customer_id}")

        # Busca diretamente pelo customer_id como string
        plans = PurchasedPlanModel.objects(customer_id=customer_id)

        print(f"🔍 Debug - Planos encontrados: {plans}")

        if not plans:
            return {"status": "error", "message": "Nenhum plano encontrado"}

        plans_dict = {
            "customer_id": customer_id,
            "plans": []
        }

        for plan in plans:
            plan_dict = plan.to_mongo().to_dict()
            plan_dict["_id"] = str(plan_dict["_id"])  # Converte _id para string
            plans_dict["plans"].append(plan_dict)

        print("✅ Debug - Retornando planos:", plans_dict)
        return plans_dict




    def update_purchased_plan(self, plan_id: str, update_data: dict) -> None:
        update_fields = {}
        for k, v in update_data.items():
            if k in PurchasedPlanModel.sensivity_fields:
                encrypted_data = self.fernet.encrypt(json.dumps(v).encode()).decode()
                update_fields[k] = encrypted_data
            else:
                update_fields[k] = v
        PurchasedPlanModel.objects(id=plan_id).update(**update_fields)

    def delete_purchased_plan(self, plan_id: str) -> None:
        PurchasedPlanModel.objects(id=plan_id).delete()

    def list_all_plans(self, customer_id: str = None) -> List[dict]:
        query = {}
        if customer_id:
            query['customer_id'] = customer_id
        plans = PurchasedPlanModel.objects(**query)
        return [plan.to_mongo().to_dict() for plan in plans]
