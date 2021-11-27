from typing import (
    Any,
    Callable,
    Type,
)

from invaultapi._util import (
    cast_dict_with_formater,
    to_self,
    to_type,
)
from invaultapi.message import (
    BlockHeightResult,
    CheckAddressResult,
    GetDepositAddressResult,
    PendingTransactionByIdResult,
    PendingTransactionsResult,
    QueryAddressesByCoinCodeResult,
    QueryAddressesInfoResult,
    QueryAssetByCodeResult,
    QueryAssetsResult,
    QueryByReqOrderIdResult,
    QueryCoinByCodeResult,
    QueryCoinsResult,
    TransactionByBlockHeightResult,
    TransactionByIdResult,
    TransactionByTxHashResult,
    TransactionsResult,
    WithdrawApplyResult,
)

_formaters = {
    QueryAssetsResult: lambda v: cast_dict_with_formater(QueryAssetsResult_FORMATER, v),
    QueryAssetByCodeResult: lambda v: cast_dict_with_formater(QueryAssetByCodeResult_FORMATER, v),
    QueryCoinsResult: lambda v: [cast_dict_with_formater(Coin_FORMATER, i) for i in v],
    QueryCoinByCodeResult: lambda v: cast_dict_with_formater(QueryCoinByCodeResult_FORMATER, v),
    QueryAddressesByCoinCodeResult: lambda v: cast_dict_with_formater(QueryAddressesByCoinCodeResult_FORMATER, v),
    QueryAddressesInfoResult: lambda v: [cast_dict_with_formater(Address_FORMATER, i) for i in v],
    CheckAddressResult: lambda v: cast_dict_with_formater(CheckAddressResult_FORMATER, v),
    GetDepositAddressResult: lambda v: [cast_dict_with_formater(Address_FORMATER, i) for i in v],
    WithdrawApplyResult: lambda v: cast_dict_with_formater(WithdrawApplyResult_FORMATER, v),
    QueryByReqOrderIdResult: lambda v: cast_dict_with_formater(QueryByReqOrderIdResult_FORMATER, v),
    TransactionsResult: lambda v: [cast_dict_with_formater(Transaction_FORMATER, i) for i in v],
    TransactionByIdResult: lambda v: cast_dict_with_formater(TransactionByIdResult_FORMATER, v),
    PendingTransactionsResult: lambda v: [cast_dict_with_formater(PendingTransaction_FORMATER, i) for i in v],
    PendingTransactionByIdResult: lambda v: cast_dict_with_formater(PendingTransactionByIdResult_FORMATER, v),
    TransactionByTxHashResult: lambda v: cast_dict_with_formater(TransactionByTxHashResult_FORMATER, v),
    BlockHeightResult: lambda v: [cast_dict_with_formater(BlockInfo_FORMATER, i) for i in v],
    TransactionByBlockHeightResult: lambda v: [cast_dict_with_formater(Transaction_FORMATER, i) for i in v],
}

def get_type_formater(typ: Type) -> Callable[[Any], Any]:
    return _formaters.get(typ, to_self)

Asset_FORMATER = {
    "assetCode": to_type(str),
    "fullLogoUrl": to_type(str),
    "assetName": to_type(str),
    "canDeposit": to_type(bool),
    "canWithdraw": to_type(bool),
    "amountUsable": to_type(str),
    "amountFrozen": to_type(str),
    "amountAll": to_type(str)
}

QueryAssetsResult_FORMATER = {
    "status": to_type(int),
    "assetList": lambda v: [cast_dict_with_formater(Asset_FORMATER, i) for i in v]
}

AssetDetail_FORMATER = {
    "network": to_type(str),
    "chainCoin": to_type(str),
    "displayDecimals": to_type(int),
    "coinAlias": to_type(str),
    "coinCode": to_type(str),
    "amountUsable": to_type(str),
    "amountFrozen": to_type(str),
    "amountAll": to_type(str),
    "canDeposit": to_type(bool),
    "canWithdraw": to_type(bool)
}

QueryAssetByCodeResult_FORMATER = {
    "assetCode": to_type(str),
    "fullLogoUrl": to_type(str),
    "assetName": to_type(str),
    "canDeposit": to_type(bool),
    "canWithdraw": to_type(bool),
    "amountUsable": to_type(str),
    "amountFrozen": to_type(str),
    "amountAll": to_type(str),
    "coinList": lambda v: [cast_dict_with_formater(AssetDetail_FORMATER, i) for i in v]
}

Coin_FORMATER = {
    "assetCode": to_type(str),
    "fullLogoUrl": to_type(str),
    "coinCode": to_type(str),
    "coinName": to_type(str),
    "coinAlias": to_type(str),
    "networkName": to_type(str),
    "decimals": to_type(int),
    "displayDecimals": to_type(str),
    "canDeposit": to_type(bool),
    "canWithdraw": to_type(bool),
    "network": to_type(str),
    "chainCoin": to_type(str),
    "feeCoin": to_type(str),
    "feeBusiness": to_type(str),
    "feeTransaction": to_type(str),
    "withdrawMin": to_type(str),
    "depositMin": to_type(str),
    "withdrawMax": to_type(str),
    "tokenAddress": to_type(str),
    "isToken": to_type(bool),
    "isMemo": to_type(bool),
    "memoRegex": to_type(str),
    "chainType": to_type(str),
    "confirmations": to_type(int),
    "amountUsable": to_type(str),
    "amountFrozen": to_type(str),
    "amountAll": to_type(str),
    "addressRegex": to_type(str),
    "label": to_type(str)
}

QueryCoinByCodeResult_FORMATER = Coin_FORMATER

Address_FORMATER = {
    "coinCode": to_type(str),
    "address": to_type(str),
    "memo": to_type(str),
}

QueryAddressesByCoinCodeResult_FORMATER = {
    "coinCode": to_type(str),
    "size": to_type(int),
    "total": to_type(int),
    "pageNum": to_type(int),
    "pageSize": to_type(int),
    "addressList": lambda v: [cast_dict_with_formater(Address_FORMATER, i) for i in v]
}

CheckAddressResult_FORMATER = {
    "coinCode": to_type(str),
    "address": to_type(str),
    "memo": to_type(str),
    "status": to_type(int)
}

GetDepositAddressResult_FORMATER = {
    "coinCode": to_type(str),
    "addressList": lambda v: [cast_dict_with_formater(Address_FORMATER, i) for i in v]
}

WithdrawApplyResult_FORMATER = {
    "success": to_type(bool),
    "message": to_type(str),
    "requestOrderId": to_type(str),
    "coinCode": to_type(str),
    "address": to_type(str),
    "memo": to_type(str),
    "amount": to_type(str),
    "timestamp": to_type(int)
}

QueryByReqOrderIdResult_FORMATER = {
    "orderNumber": to_type(str),
    "externalOrderId": to_type(str),
    "orderType": to_type(str),
    "orderStatus": to_type(int),
    "description": to_type(str),
    "orderTimeStamp": to_type(str),
    "coinCode": to_type(str),
    "assetCode": to_type(str),
    "fromAddress": to_type(str),
    "toAddress": to_type(str),
    "amount": to_type(str),
    "memo": to_type(str),
    "transactionFee": to_type(str),
    "feeCoin": to_type(str),
    "orderFee": to_type(str),
    "transactionHash": to_type(str),
    "transactionStatus": to_type(int),
    "transactionType": to_type(str),
    "blockHeight": to_type(int),
    "blockHash": to_type(str),
    "chainCoin": to_type(str),
    "tokenAddress": to_type(str),
    "transactionIndex": to_type(str)
}

Transaction_FORMATER = {
    "custodyOrderId": to_type(str),
    "coinCode": to_type(str),
    "coinName": to_type(str),
    "coinName": to_type(str),
    "toAddress": to_type(str),
    "addressSourceType": to_type(str),
    "memo": to_type(str),
    "orderType": to_type(str),
    "orderStatus": to_type(int),
    "orderTimestamp": to_type(str),
    "endTime": to_type(int),
    "amount": to_type(str),
    "orderAmount": to_type(str),
    "feeCoin": to_type(str),
    "orderFee": to_type(str),
    "transactionHash": to_type(str),
    "blockHeight": to_type(str),
    "blockHash": to_type(str),
    "chainCoin": to_type(str),
    "tokenAddress": to_type(str),
    "timeStamp": to_type(int),
    "transactionStatus": to_type(int),
    "transactionIndex": to_type(str)
}

TransactionByIdResult_FORMATER = Transaction_FORMATER

TransactionByTxHashResult_FORMATER = Transaction_FORMATER

PendingTransaction_FORMATER = {
    "custodyOrderId": to_type(str),
    "coinCode": to_type(str),
    "coinName": to_type(str),
    "assetCode": to_type(str),
    "decimals": to_type(int),
    "toAddress": to_type(str),
    "addressSourceType": to_type(str),
    "memo": to_type(str),
    "orderType": to_type(str),
    "orderStatus": to_type(int),
    "orderTimestamp": to_type(str),
    "endTime": to_type(int),
    "amount": to_type(str),
    "feeCoin": to_type(str),
    "orderFee": to_type(str),
    "transactionHash": to_type(str),
    "blockHeight": to_type(str),
    "blockHash": to_type(str),
    "chainCoin": to_type(str),
    "tokenAddress": to_type(str),
    "timeStamp": to_type(int),
    "transactionStatus": to_type(int),
    "transactionIndex": to_type(str),
    "confirmingThreshold": to_type(int),
    "confirmedNum": to_type(int)
}

PendingTransactionByIdResult_FORMATER = PendingTransaction_FORMATER

BlockInfo_FORMATER = {
    "coinCode": to_type(str),
    "blockHeight": to_type(str),
    "chainCoin": to_type(str)
}
