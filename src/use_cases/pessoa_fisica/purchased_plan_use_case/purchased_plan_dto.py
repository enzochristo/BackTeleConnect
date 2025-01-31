from pydantic import BaseModel
from typing import Literal, Optional

class PurchasedPlanDTO(BaseModel):
    plan_type: str
    speed: Optional[int] = None
    final_price: float
    cep: str
    rua: str
    cidade: str
    numero: str
    estado: str
