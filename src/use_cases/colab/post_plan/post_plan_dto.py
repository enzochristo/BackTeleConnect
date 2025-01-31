from pydantic import BaseModel
from typing import Optional

class PostPlanDTO(BaseModel):
    name: str
    tipo: str
    vel_max: Optional[int] = None
    vel_min: Optional[int] = None
    price: float
    benefits: Optional[str] = None
