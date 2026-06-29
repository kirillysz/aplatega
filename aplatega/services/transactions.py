from aplatega.client.base import AplategaClient
from aplatega.core.types import CreateTransactionRequest


class TransactionsService:
    def __init__(self, client: AplategaClient):
        self.client = client

    async def get_h2h(self, payment_id: str):
        return await self.client.get(
            f"/h2h/{payment_id}"
        )
    
    async def get_transaction(self, payment_id: str):
        return await self.client.get(
            f"/transaction/{payment_id}"
        )

    async def create_transaction(
        self,
        data: CreateTransactionRequest,
    ):
        return await self.client.post(
            "/transaction/process",
            json=data
        )

    async def create_transaction_without_method(
        self,
        data: CreateTransactionRequest,
    ):
        return await self.client.post(
            "v2/transaction/process",
            json=data
        )
    
    