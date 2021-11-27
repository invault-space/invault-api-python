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

class Assets:
    def __init__(self, provider: ClientBase):
        self.provider = provider
        self.caller = partial(rpc_method_caller, self.provider)

    def query_assets(self, params):
        return self.caller(*abi.QueryAssets)(params)

    def query_asset_by_code(self, params):
        return self.caller(*abi.QueryAssetByCode)(params)

    def query_coins(self, params):
        return self.caller(*abi.QueryCoins)(params)

    def query_coin_by_code(self, params):
        return self.caller(*abi.QueryCoinByCode)(params)

    def query_addresses_by_coin_code(self, params):
        return self.caller(*abi.QueryAddressesByCoinCode)(params)

    def query_addresses_info(self, params):
        return self.caller(*abi.QueryAddressesInfo)(params)

    def check_address(self, params):
        return self.caller(*abi.CheckAddress)(params)

    def get_deposit_address(self, params):
        return self.caller(*abi.GetDepositAddress)(params)

class AsyncAssets:
    def __init__(self, provider: AsyncClientBase):
        self.provider = provider
        self.caller = partial(async_rpc_method_caller, self.provider)

    async def query_assets(self, params):
        return await self.caller(*abi.QueryAssets)(params)

    async def query_asset_by_code(self, params):
        return self.caller(*abi.QueryAssetByCode)(params)

    async def query_coins(self, params):
        return await self.caller(*abi.QueryCoins)(params)

    async def query_coin_by_code(self, params):
        return await self.caller(*abi.QueryCoinByCode)(params)

    async def query_addresses_by_coin_code(self, params):
        return await self.caller(*abi.QueryAddressesByCoinCode)(params)

    async def query_addresses_info(self, params):
        return await self.caller(*abi.QueryAddressesInfo)(params)

    async def check_address(self, params):
        return await self.caller(*abi.CheckAddress)(params)

    async def get_deposit_address(self, params):
        return await self.caller(*abi.GetDepositAddress)(params)
