from pydantic import BaseModel
from typing import List, Optional
from models.product_models import ProductIn
from db.orders_db import OrderInDB
from utils.pay_methods import PayMethod


class OrderIn(BaseModel):
    client_id: Optional[str] = None
    pay_method: PayMethod
    products: List[ProductIn]


class OrderOut(BaseModel):
    order_id: str
    detail: OrderInDB
