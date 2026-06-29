from aplatega.client.base import BaseClient

class BalancesService:
    def __init__(self, client: BaseClient):
        self.client = client

    async def get_balances(self):
        return await self.client.get(
            "/balance/all"
        )
