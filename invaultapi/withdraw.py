from functools import partial

import invaultapi.abi as abi
from invaultapi.method import (
    async_rpc_method_caller,
    rpc_method_caller,
)
from invaultapi.rpc import (
    ClientBase,
    AsyncClientBase,
)


class Withdraw:
    def __init__(self, provider: ClientBase):
        self.provider = provider
        self.caller = partial(rpc_method_caller, self.provider)

    def withdraw_apply(self, params):
        return self.caller(*abi.WithdrawApply)(params)

    def query_by_req_order_id(self, params):
        return self.caller(*abi.QueryByReqOrderId)(params)

class AsyncWithdraw:
    def __init__(self, provider: AsyncClientBase):
        self.provider = provider
        self.caller = partial(async_rpc_method_caller, self.provider)

    async def withdraw_apply(self, params):
        return await self.caller(*abi.WithdrawApply)(params)

    async def query_by_req_order_id(self, params):
        return await self.caller(*abi.QueryByReqOrderId)(params)
