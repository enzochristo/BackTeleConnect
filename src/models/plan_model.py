from mongoengine import *
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PlanModel(Document):
    sensivity_fields = []
    
    name = StringField(required=True)
    tipo = StringField(required=True, choices=["Internet", "Mobile", "Fixed"])
    price = FloatField(required=True)
    benefits = StringField()
    vel_max = IntField(required=False)
    vel_min = IntField(required=False)
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def get_normal_fields():
        return [i for i in PlanModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields"]
