
from typing import Any

from invaultapi.rpc import RPCEndpoint


class ClientBase:
    def call(self, method: RPCEndpoint, params: Any):
        raise NotImplementedError("method call not implemented")

class AsyncClientBase:
    async def call(self, method: RPCEndpoint, params: Any):
        raise NotImplementedError("method call not implemented")
