import dotenv
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

dotenv.load_dotenv()

class Plan(BaseModel):
    _id: str # O ID pode ser gerado pelo banco
    name: str  # Nome do plano
    tipo: Literal["Internet", "Mobile", "Fixed"]
    vel_max: Optional[int] = None
    vel_min: Optional[int] = None
    price: float
    benefits: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
