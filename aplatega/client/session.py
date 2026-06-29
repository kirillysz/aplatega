import aiohttp
from typing import Optional

class SessionManager:
    def __init__(self, timeout: int):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session: Optional[aiohttp.ClientSession] = None

    async def open(self, headers: dict):
        if not self.session:
            self.session = aiohttp.ClientSession(
                timeout=self.timeout,
                headers=headers,
            )

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None