from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cliente(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    created_at: Optional[datetime] = None
