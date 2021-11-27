from invaultapi.message import (
    QueryAssetsParams,
    QueryAssetsResult,
    QueryAssetByCodeParams,
    QueryAssetByCodeResult,
    QueryCoinsParams,
    QueryCoinsResult,
    QueryCoinByCodeParams,
    QueryCoinByCodeResult,
    QueryAddressesByCoinCodeParams,
    QueryAddressesByCoinCodeResult,
    QueryAddressesInfoParams,
    QueryAddressesInfoResult,
    CheckAddressParams,
    CheckAddressResult,
    GetDepositAddressParams,
    GetDepositAddressResult,
    WithdrawApplyParams,
    WithdrawApplyResult,
    QueryByReqOrderIdParams,
    QueryByReqOrderIdResult,
    TransactionsParams,
    TransactionsResult,
    TransactionByIdParams,
    TransactionByIdResult,
    TransactionByTxHashParams,
    TransactionByTxHashResult,
    TransactionByBlockHeightParams,
    TransactionByBlockHeightResult,
    PendingTransactionsParams,
    PendingTransactionsResult,
    PendingTransactionByIdParams,
    PendingTransactionByIdResult,
    BlockHeightParams,
    BlockHeightResult,
)
from invaultapi.rpc import RPCEndpoint

QueryAssets = tuple([RPCEndpoint("queryAssets"), QueryAssetsParams, QueryAssetsResult])
QueryAssetByCode = tuple([RPCEndpoint("queryAssetByCode"), QueryAssetByCodeParams, QueryAssetByCodeResult])
QueryCoins = tuple([RPCEndpoint("queryCoins"), QueryCoinsParams, QueryCoinsResult])
QueryCoinByCode = tuple([RPCEndpoint("queryCoinByCode"), QueryCoinByCodeParams, QueryCoinByCodeResult])
QueryAddressesByCoinCode = tuple([RPCEndpoint("queryAddressesByCoinCode"), QueryAddressesByCoinCodeParams, QueryAddressesByCoinCodeResult])
QueryAddressesInfo = tuple([RPCEndpoint("queryAddressesInfo"), QueryAddressesInfoParams, QueryAddressesInfoResult])
CheckAddress = tuple([RPCEndpoint("checkAddress"), CheckAddressParams, CheckAddressResult])
GetDepositAddress = tuple([RPCEndpoint("getDepositAddress"), GetDepositAddressParams, GetDepositAddressResult])
WithdrawApply = tuple([RPCEndpoint("withdrawApply"), WithdrawApplyParams, WithdrawApplyResult])
QueryByReqOrderId = tuple([RPCEndpoint("queryByReqOrderId"), QueryByReqOrderIdParams, QueryByReqOrderIdResult])
Transactions = tuple([RPCEndpoint("transactions"), TransactionsParams, TransactionsResult])
TransactionById = tuple([RPCEndpoint("transactionById"), TransactionByIdParams, TransactionByIdResult])
TransactionByTxHash = tuple([RPCEndpoint("transactionByTxHash"), TransactionByTxHashParams, TransactionByTxHashResult])
TransactionByBlockHeight = tuple([RPCEndpoint("transactionByBlockHeight"), TransactionByBlockHeightParams, TransactionByBlockHeightResult])
PendingTransactions = tuple([RPCEndpoint("pendingTransactions"), PendingTransactionsParams, PendingTransactionsResult])
PendingTransactionById = tuple([RPCEndpoint("pendingTransactionById"), PendingTransactionByIdParams, PendingTransactionByIdResult])
BlockHeight = tuple([RPCEndpoint("blockHeight"), BlockHeightParams, BlockHeightResult])
