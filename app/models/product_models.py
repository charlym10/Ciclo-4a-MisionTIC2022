from pydantic import BaseModel


class ProductIn(BaseModel):
    product_id: int
    amount: int
