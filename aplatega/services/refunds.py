from aplatega.client.base import BaseClient

class RefundsService:
    def __init__(self, client: BaseClient):
        self.client = client

    async def is_cancel_supported(self, payment_id):
        return await self.client.get(
            f"/transaction/{payment_id}/cancel_supported"
        )
    
    async def cancel_payment(self, payment_id):
        return await self.client.post(
            f"/transaction/{payment_id}/cancel"
        )