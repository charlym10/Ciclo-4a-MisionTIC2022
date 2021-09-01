from pydantic import BaseModel
from models.order_models import OrderOut
from typing import List


class OrdersOut(BaseModel):
    orsders: List[OrderOut]
