from dataclasses import dataclass
from aplatega.core.enums import PaymentStatus

@dataclass
class Payment:
    id: str
    amount: int
    currency: str
    status: PaymentStatus

@dataclass
class Rate:
    payment_method: int
    currency_from: str
    currency_to: str
    rate: float
    updated_at: str

@dataclass
class Transaction:
    id: str
    status: PaymentStatus
    amount: int
    currency: str
    payment_method: int


@dataclass
class PaymentCallback:
    id: str
    amount: float
    currency: str
    status: PaymentStatus
    payment_method: int

def parse_payment(data: dict) -> Payment:
    return Payment(
        id=data["id"],
        amount=data["amount"],
        currency=data["currency"],
        status=PaymentStatus(data["status"]),
    )