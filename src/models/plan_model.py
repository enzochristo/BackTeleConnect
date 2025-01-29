from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PlansModel(Document):
    sensivity_fields = [
        
    ]

    name = StringField(required=True)
    customer_id = StringField(required=True)
    tipo = StringField(required=True)
    price = FloatField(required = True)
    benefits = StringField()
    created_at: DateTimeField(default=datetime.utcnow)
    updated_at: DateTimeField()


    def get_normal_fields():
        return [i for i in PlansModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in PlanModel.sensivity_fields]
    
