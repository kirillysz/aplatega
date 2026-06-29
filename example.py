import asyncio
from aplatega import Aplatega
from aplatega.core.enums import PaymentMethod

async def main():
    async with Aplatega(
        base_url="https://app.platega.io",
        merchant_id="123",
        secret="abc"
    ) as api:

        rates = await api.rates.get_rates_by_method(
            payment_method=PaymentMethod.SBP,
            currency_from="RUB",
            currency_to="USDT"
        )

        print(rates)

asyncio.run(main())