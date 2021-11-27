from invaultapi._util import (
    Literal,
    TypedDict,
)

from typing import (
    Any,
    NewType,
    Optional,
    Union,
)

RPCEndpoint = NewType("RPCEndpoint", str)

class RPCError(TypedDict):
    code: int
    message: str
    data: Optional[str]

class RPCResponse(TypedDict, total=False):
    jsonrpc: Literal["2.0"]
    id: Union[int, str]
    method: Optional[str]
    result: Optional[Any]
    error: Optional[Union[RPCError, str]]
