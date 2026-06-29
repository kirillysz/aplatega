from aplatega.client.base import BaseClient
from aplatega.core.enums import PaymentMethod


class RatesService:
    def __init__(self, client: BaseClient):
        self.client = client

    async def get_rates_by_method(
        self,
        payment_method: PaymentMethod,
        currency_from: str,
        currency_to: str,
    ):
        return await self.client.get(
            "/rates/payment_method_rate",
            params={
                "paymentMethod": payment_method.value,
                "currency_from": currency_from,
                "currency_to": currency_to,
            }
        )