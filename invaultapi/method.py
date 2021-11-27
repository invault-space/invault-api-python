
from typing import (
    Any,
    Dict,
    Type,
)

from invaultapi.message_format import get_type_formater
from invaultapi.rpc import (
    AsyncClientBase,
    ClientBase,
    RPCEndpoint,
)


def rpc_method_caller(provider: ClientBase, method: RPCEndpoint, params_type: Type, result_type: Type):
    def caller(params: Any) -> Dict:
        params_formater = get_type_formater(params_type)
        r = provider.call(method, params_formater(params))
        error = r.get("error")
        if error is not None:
            raise RuntimeError(error)
        result_formater = get_type_formater(result_type)
        return result_formater(r.get("result"))
    return caller

def async_rpc_method_caller(provider: AsyncClientBase, method: RPCEndpoint, params_type: Type, result_type: Type):
    async def caller(params: Any) -> Dict:
        params_formater = get_type_formater(params_type)
        r = await provider.call(method, params_formater(params))
        error = r.get("error")
        if error is not None:
            raise RuntimeError(error)
        result_formater = get_type_formater(result_type)
        return result_formater(r.get("result"))
    return caller