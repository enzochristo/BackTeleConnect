import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.plan import Plan
from models.plan_model import PlanModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class PlanRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, plan: Plan) -> None:
        plan_model = PlanModel()
        plan_dict = plan.model_dump()

        for k in PlanModel.get_normal_fields():
            if (k not in plan_dict):
                continue

            plan_model[k] = plan_dict[k]

        for k in PlanModel.sensivity_fields:
            plan_model[k] = SensivityField(fernet=self.fernet, data=plan_dict[k])

    

        plan_model.save()

        return None
    
    def get_plan_by_id(self, plan_id: str) -> dict:
        plan = PlanModel.objects.with_id(plan_id)
        if not plan:
            return None
        plan_dict = plan.to_mongo().to_dict()
        plan_dict['_id'] = str(plan_dict['_id'])
        return plan_dict
    

    def delete_plan(self, plan_id: str):
        PlanModel.objects(id=plan_id).delete()
        return None