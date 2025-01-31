import os
import dotenv
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

dotenv.load_dotenv()

class PurchasedPlan(BaseModel):
    _id: str
    customer_id: str
    plan_type: Literal["Internet", "Mobile", "Fixed"]
    speed: Optional[int] = None
    final_price: float
    created_at: datetime
    updated_at: Optional[datetime] = None
    cep: str
    rua: str
    cidade: str
    numero: str
    estado: str
