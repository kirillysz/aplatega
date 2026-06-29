from enum import Enum

class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELED = "CANCELED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"
    CHARGEBACKED = "CHARGEBACKED"

class PaymentMethod(int, Enum):
    SBP = 2
    CARD_RU = 10
    INTERNATIONAL = 12
    CRYPTO = 13

