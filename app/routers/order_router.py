from db.orders_db import OrderInDB, ProductInDB
from fastapi import APIRouter
from models.order_models import OrderIn, OrderOut
from db.db_conection import database
from random import randint
from utils.compute_points import compute_points


router = APIRouter()


@router.post('/api/v1/order')
async def order(order_in: OrderIn):

    products: list = []
    subtotal: float = 0
    total: float = 0

    for item in order_in.products:

        # Conultar al microservicio de productos (Pendiente).
        unit_price: float = randint(5000, 15000)
        iva: float = 0.19

        # Verificar disponibilidad y ajustar inventario (Pendiente).

        subtotal_price: float = item.amount * unit_price
        total_price: float = subtotal_price * (1 + iva)

        data = {
            'product_id': item.product_id,
            'amount': item.amount,
            'unit_price': unit_price,
            'iva': iva,
            'subtotal_price': subtotal_price,
            'total_price': total_price
        }

        product = ProductInDB(**data)

        products.append(product)

        subtotal += subtotal_price
        total += total_price

    points: int = compute_points(subtotal)

    data = {
        'client_id': order_in.client_id,
        'pay_method': order_in.pay_method,
        'products': products,
        'subtotal': subtotal,
        'total': total,
        'points': points
    }

    order = OrderInDB(**data)

    order_id = database.orders.insert_one(order.dict()).inserted_id

    data = {
        'order_id': str(order_id),
        'detail': order
    }

    order_out = OrderOut(**data)

    # Acumular puntos si el usuario está registrado (Pendiente).

    return order_out
