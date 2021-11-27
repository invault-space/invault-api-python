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


class Transaction:
    def __init__(self, provider: ClientBase):
        self.provider = provider
        self.caller = partial(rpc_method_caller, self.provider)

    def transactions(self, params):
        return self.caller(*abi.Transactions)(params)

    def transaction_by_id(self, params):
        return self.caller(*abi.TransactionById)(params)

    def transaction_by_tx_hash(self, params):
        return self.caller(*abi.TransactionByTxHash)(params)

    def transaction_by_block_height(self, params):
        return self.caller(*abi.TransactionByBlockHeight)(params)
    
    def pending_transactions(self, params):
        return self.caller(*abi.PendingTransactions)(params)

    def pending_transaction_by_id(self, params):
        return self.caller(*abi.PendingTransactionById)(params)

    def block_height(self, params):
        return self.caller(*abi.BlockHeight)(params)

class AsyncTransaction:
    def __init__(self, provider: AsyncClientBase):
        self.provider = provider
        self.caller = partial(async_rpc_method_caller, self.provider)

    async def transactions(self, params):
        return await self.caller(*abi.Transactions)(params)

    async def transaction_by_id(self, params):
        return await self.caller(*abi.TransactionById)(params)

    async def transaction_by_tx_hash(self, params):
        return await self.caller(*abi.TransactionByTxHash)(params)

    async def transaction_by_block_height(self, params):
        return await self.caller(*abi.TransactionByBlockHeight)(params)
    
    async def pending_transactions(self, params):
        return await self.caller(*abi.PendingTransactions)(params)

    async def pending_transaction_by_id(self, params):
        return await self.caller(*abi.PendingTransactionById)(params)

    async def block_height(self, params):
        return await self.caller(*abi.BlockHeight)(params)
