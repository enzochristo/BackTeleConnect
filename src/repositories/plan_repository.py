import os
import bcrypt
import dotenv
from bson import ObjectId
from typing import List
from fastapi import HTTPException
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
    
    from bson import ObjectId

    def delete_plan(self, plan_id: str):
        # Validar se o ID fornecido é válido
        if not ObjectId.is_valid(plan_id):
            raise HTTPException(status_code=400, detail="ID inválido")

        # Buscar o plano com o ID convertido
        plan = PlanModel.objects(id=ObjectId(plan_id)).first()
        if not plan:
            raise HTTPException(status_code=404, detail="Plano não encontrado")

        # Deletar o plano se encontrado
        plan.delete()
        return {"status": "success", "message": "Plano deletado com sucesso"}

        
    def list_all_plans(self) -> List[dict]:
        try:
            plans = PlanModel.objects()
            return [
                {**plan.to_mongo().to_dict(), "_id": str(plan.id)}
                for plan in plans
            ]
        except Exception as e:
            raise Exception(f"Error fetching plans: {str(e)}")
            
   

    def update_plan(self, plan_id: str, price: float = None, tipo: str = None, benefits: str = None) -> dict:
        if not ObjectId.is_valid(plan_id):
            raise HTTPException(status_code=400, detail="ID inválido")

        # Montar os campos para atualização
        update_fields = {}
        if price is not None:
            update_fields["set__price"] = price
        if tipo is not None:
            update_fields["set__tipo"] = tipo
        if benefits is not None:
            update_fields["set__benefits"] = benefits

        if not update_fields:
            raise ValueError("Nenhum campo válido para atualização.")

        updated_count = PlanModel.objects(id=ObjectId(plan_id)).update(**update_fields)

        if updated_count == 0:
            raise HTTPException(status_code=404, detail="Plano não encontrado.")

        return self.get_plan_by_id(plan_id)