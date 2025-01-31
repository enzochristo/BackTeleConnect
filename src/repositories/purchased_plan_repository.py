import os
from mongoengine import *
from entities.purchased_plan import PurchasedPlan
from models.purchased_plan_model import PurchasedPlanModel
from cryptography.fernet import Fernet
import json
from typing import List


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

    def get_purchased_plan_by_id(self, plan_id: str) -> dict:
        plan = PurchasedPlanModel.objects.with_id(plan_id)
        if not plan:
            return None
        plan_dict = plan.to_mongo().to_dict()
        for k in PurchasedPlanModel.sensivity_fields:
            if k in plan_dict:
                decrypted_data = json.loads(self.fernet.decrypt(plan_dict[k].encode()).decode())
                plan_dict[k] = decrypted_data
        return plan_dict

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
