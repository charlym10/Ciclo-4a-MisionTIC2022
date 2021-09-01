from enum import Enum


class PayMethod(str, Enum):
    cash = 'cash'
    credit_card = 'credit_card'
