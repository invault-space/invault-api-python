import functools
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
)

import aiohttp
import requests

from invaultapi.rpc import (
    AsyncClientBase,
    ClientBase,
    JSONParams,
    RPCEndpoint,
    RPCResponse,
)

class _Session(requests.Session):
    def __init__(self):
        super().__init__()

    def __del__(self):
        self.close()

@functools.lru_cache(8)
def _get_session(url: str) -> _Session:
    return _Session()

def default_headers_fn(**kwargs) -> Optional[Dict]:
    return kwargs.get("headers")

def get_headers(**kwargs) -> Dict:
    headers = kwargs.get("headers")
    if headers is None:
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
    if callable(headers):
        return headers(**kwargs)
    return headers

def request_post(url: str, data: bytes, *args: Any, **kwargs: Any) -> bytes:
    kwargs.setdefault("timeout", 10)
    kwargs["headers"] = get_headers(data = data, **kwargs)
    session = _get_session(url)
    # https://github.com/python/mypy/issues/2582
    response = session.post(url, data=data, *args, **kwargs)  # type: ignore
    response.raise_for_status()
    return response.content

async def async_request_post(url: str, data: bytes, *args: Any, **kwargs: Any) -> bytes:
    kwargs.setdefault("timeout", aiohttp.ClientTimeout(10))
    kwargs["headers"] = get_headers(data = data, **kwargs)
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        async with session.post(url, data=data, *args, **kwargs) as response:
            return await response.read()

class HTTPClient(ClientBase):
    def __init__(self, url, headers_fn = default_headers_fn):
        self.url = url
        self.headers_fn = headers_fn

    def call(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        data = JSONParams.encode_rpc_request(method, params)
        raw_response = request_post(self.url, data = data, headers = self.headers_fn)
        return JSONParams.decode_rpc_response(raw_response)

class AsyncHTTPClient(AsyncClientBase):
    def __init__(self, url, headers_fn: Callable[[Dict[str, Any]], Dict] = default_headers_fn):
        self.url = url
        self.headers_fn = headers_fn

    async def call(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        data = JSONParams.encode_rpc_request(method, params)
        raw_response = await async_request_post(self.url, data = data, headers = self.headers_fn)
        return JSONParams.decode_rpc_response(raw_response)
