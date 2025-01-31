from mongoengine import Document, StringField, FloatField, DateTimeField, IntField
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PurchasedPlanModel(Document):
    sensivity_fields = []

    customer_id = StringField(required=True)
    plan_type = StringField(required=True, choices=["Internet", "Mobile", "Fixed"])
    speed = IntField(required=False, default= None)
    final_price = FloatField(required=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()
    
    cep = StringField(required=True)
    rua = StringField(required=True)
    cidade = StringField(required=True)
    numero = StringField(required=True)
    estado = StringField(required=True)

    def get_normal_fields(cls):
        return [field for field in cls._fields_ordered if field not in cls.sensivity_fields]
