from pydantic import BaseModel
from typing import List, Optional
from utils.pay_methods import PayMethod


class ProductInDB(BaseModel):
    product_id: int
    amount: int
    unit_price: float
    iva: float
    subtotal_price: float
    total_price: float


class OrderInDB(BaseModel):
    client_id: Optional[str]
    pay_method: PayMethod
    products: List[ProductInDB]
    subtotal: float
    total: float
    points: Optional[int]
