from typing import Dict

class Auth:
    def __init__(self, merchant_id: str, secret: str):
        self.merchant_id = merchant_id
        self.secret = secret

    def headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "X-MerchantId": self.merchant_id,
            "X-Secret": self.secret
        }