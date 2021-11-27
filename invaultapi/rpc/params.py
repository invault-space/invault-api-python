import itertools
import json
from typing import (
    Any,
)
from invaultapi.rpc.format import format_rpc_response

from invaultapi.rpc import (
    RPCEndpoint,
    RPCResponse,
)

class JSONParams:
    request_counter = itertools.count(start = 1)

    @classmethod
    def encode_rpc_request(cls, method: RPCEndpoint, params: Any) -> bytes:
        rpc_dict = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(cls.request_counter)
        }
        return json.dumps(rpc_dict, separators = (",", ":"), sort_keys = True).encode("utf8")

    @classmethod
    def decode_rpc_response(cls, raw_response: bytes) -> RPCResponse:
        return format_rpc_response(json.loads(raw_response))
