import asyncio
from typing import Any, Dict, Optional

import aiohttp

from aplatega.client.auth import Auth
from aplatega.client.config import ClientConfig
from aplatega.client.session import SessionManager
from aplatega.core.exceptions import APIError

class BaseClient():
    def __init__(self, config: ClientConfig):
        self.config = config

        self.auth = Auth(config.merchant_id, config.secret)
        self.session = SessionManager(config.timeout)

        self.base_url = config.base_url.rstrip("/")


    async def __aenter__(self):
        await self.session.open(self.auth.headers())
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:

        if not self.session.session:
            raise RuntimeError("Client not initialized. Use async with.")

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        for attempt in range(self.config.retry_attempts + 1):
            try:
                async with self.session.session.request(
                    method,
                    url,
                    json=json,
                    params=params,
                    headers=self.auth.headers()
                ) as response:

                    try:
                        data = await response.json(content_type=None)
                    except Exception:
                        data = await response.text()

                    if 200 <= response.status < 300:
                        return data

                    raise APIError(
                        f"HTTP {response.status}",
                        details=data
                    )

            except aiohttp.ClientError as e:
                if attempt == self.config.retry_attempts:
                    raise APIError(f"Network error: {e}")

                await asyncio.sleep(0.5 * (attempt + 1))

    async def get(self, endpoint: str, params=None):
        return await self.request("GET", endpoint, params=params)

    async def post(self, endpoint: str, json=None):
        return await self.request("POST", endpoint, json=json)

    async def put(self, endpoint: str, json=None):
        return await self.request("PUT", endpoint, json=json)

    async def delete(self, endpoint: str, json=None):
        return await self.request("DELETE", endpoint, json=json)