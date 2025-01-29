import dotenv
from pydantic import BaseModel
from typing import Literal, Optional
import datetime
dotenv.load_dotenv()

class Plan(BaseModel):
    _id: str
    customer_id: str
    name: Literal["5G", "Teleconnect Móvel", "Teleconnect Fixo"]
    tipo: Literal["Internet", "Mobile", "Fixed"]
    price: float
    benefits: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime]
