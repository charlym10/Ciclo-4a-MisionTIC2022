from typing import List
from fastapi import APIRouter
from db.db_conection import database
from models.orders_models import OrdersOut
from models.order_models import OrderOut
from db.orders_db import OrderInDB


router = APIRouter()


@router.get('/api/v1/orders')
async def get_orders():
    data = database.orders.find()

    orders: OrdersOut = []

    for i in data:
        order_id = i['_id']
        detail = OrderInDB(**i)
        order = OrderOut(order_id=str(order_id), detail=detail)
        orders.append(order)
    
    return orders
