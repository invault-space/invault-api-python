from invaultapi._util import (
    cast_dict_with_formater,
    to_self,
    to_type,
)
from invaultapi.rpc import RPCResponse

def format_rpc_response(response: dict) -> RPCResponse:
    return RPCResponse(**cast_dict_with_formater(RPC_RESPONSE_FORMATER, response))

RPC_ERROR_FORMATER = {
    "code": to_type(int),
    "message": to_type(str),
    "data": to_type(str)
}

RPC_RESPONSE_FORMATER = {
    "id": to_type(int),
    "jsonrpc": to_type(str),
    "method": to_type(str),
    "result": to_self,
    "error": lambda v: cast_dict_with_formater(RPC_ERROR_FORMATER, v) if isinstance(v, dict) else v,
}
