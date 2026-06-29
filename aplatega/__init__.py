from aplatega.client.base import BaseClient
from aplatega.client.config import ClientConfig
from aplatega.services.rates import RatesService


class Aplatega:
    def __init__(
        self,
        base_url: str,
        merchant_id: str,
        secret: str,
        timeout: int = 10,
        retry_attempts: int = 3,
    ):
        self._config = ClientConfig(
            base_url=base_url,
            merchant_id=merchant_id,
            secret=secret,
            timeout=timeout,
            retry_attempts=retry_attempts,
        )
        self._client = BaseClient(self._config)
        
        self.rates = RatesService(self._client)

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._client.__aexit__(exc_type, exc, tb)