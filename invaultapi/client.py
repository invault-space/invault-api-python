from datetime import datetime
from functools import partial
from typing import (
    Dict,
)

from invaultapi._util import RSAKey
from invaultapi.assets import (
    Assets,
    AsyncAssets
)
from invaultapi.rpc import (
    AsyncHTTPClient,
    HTTPClient,
)
from invaultapi.transaction import (
    AsyncTransaction,
    Transaction,
)
from invaultapi.withdraw import (
    AsyncWithdraw,
    Withdraw,
)


def generate_headers_with_signature(rsa: RSAKey, keyid: str, data: bytes, **kwargs) -> Dict:
    headers = {
        "keyStr": keyid,
        "sign": rsa.sign(data).hex(),
        "timestamp": str(int(datetime.utcnow().timestamp()*1000)),
        "Content-Type": "application/json;charset=UTF-8"
    }
    return headers

class Client:
    def __init__(self, url: str, key_to_sign: str, keyid: str):
        self.rsa = RSAKey.import_key(key_to_sign)
        self.keyid = keyid
        self.headers_fn = partial(generate_headers_with_signature, self.rsa, keyid)
        self.provider = HTTPClient(url, headers_fn = self.headers_fn)
        self.assets = Assets(self.provider)
        self.withdraw = Withdraw(self.provider)
        self.transaction = Transaction(self.provider)

class AsyncClient:
    def __init__(self, url: str, key_to_sign: str, keyid: str):
        self.rsa = RSAKey.import_key(key_to_sign)
        self.keyid = keyid
        self.headers_fn = partial(generate_headers_with_signature, self.rsa, keyid)
        self.provider = AsyncHTTPClient(url, headers_fn = self.headers_fn)
        self.assets = AsyncAssets(self.provider)
        self.withdraw = AsyncWithdraw(self.provider)
        self.transaction = AsyncTransaction(self.provider)

