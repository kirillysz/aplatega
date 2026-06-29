from dataclasses import dataclass

@dataclass
class ClientConfig:
    base_url: str
    merchant_id: str
    secret: str
    timeout: int = 10
    retry_attempts: int = 3