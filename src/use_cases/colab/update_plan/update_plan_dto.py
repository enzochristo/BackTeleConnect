from pydantic import BaseModel
from typing import Optional

class UpdatePlanDTO(BaseModel):
    tipo: Optional[str]
    price: Optional[float]
    benefits: Optional[str]
