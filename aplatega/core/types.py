from typing import TypedDict, Optional, Any

class PaymentRaw(TypedDict):
    id: str
    amount: int
    currency: str
    status: str

class PaymentDetails(TypedDict):
    amount: int
    currency: str


class CreateTransactionRequest(TypedDict):
    paymentMethod: Optional[int]
    paymentDetails: PaymentDetails

    description: str
    returnUrl: str
    failedUrl: str
    payload: str
    
    metadata: Optional[dict[str, Any]]

class CreateTransactionResponse(TypedDict):
    transactionId: str
    status: str
    url: str
    expiresIn: str
    rate: float



class RateResponse(TypedDict):
    paymentMethod: int
    currencyFrom: str
    currencyTo: str
    rate: float
    updatedAt: str


class TransactionDetailsResponse(TypedDict):
    id: str
    status: str
    paymentDetails: dict[str, Any]

    merchantName: str
    merchantId: str

    paymentMethod: int
    expiresIn: str
    payload: Optional[str]

class CallbackPayload(TypedDict):
    id: str
    amount: float
    currency: str
    status: str
    paymentMethod: int