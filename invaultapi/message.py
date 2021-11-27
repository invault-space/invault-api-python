from typing import (
    List,
    NewType,
    Optional,
)

from invaultapi._util import TypedDict

class EmptyParams(TypedDict):
    pass

class QueryAssetsParams(EmptyParams):
    pass

class Asset(TypedDict):
    assetCode: str
    fullLogoUrl: str
    assetName: str
    canDeposit: bool
    canWithdraw: bool
    amountUsable: str
    amountFrozen: str
    amountAll: str

class QueryAssetsResult(TypedDict):
    status: int
    assetList: List[Asset]

class QueryAssetByCodeParams(TypedDict):
    assetCode: str

class AssetDetail(TypedDict):
    network: str
    chainCoin: str
    displayDecimals: int
    coinAlias: str
    coinCode: str
    amountUsable: str
    amountFrozen: str
    amountAll: str
    canDeposit: bool
    canWithdraw: bool

class QueryAssetByCodeResult(TypedDict):
    assetCode: str
    fullLogoUrl: str
    assetName: str
    canDeposit: bool
    canWithdraw: bool
    amountUsable: str
    amountFrozen: str
    amountAll: str
    coinList: List[AssetDetail]

class QueryCoinsParams(EmptyParams):
    pass

class Coin(TypedDict):
    assetCode: str
    fullLogoUrl: str
    coinCode: str
    coinName: str
    coinAlias: str
    networkName: str
    decimals: int
    displayDecimals: str
    canDeposit: bool
    canWithdraw: bool
    network: str
    chainCoin: str
    feeCoin: str
    feeBusiness: str
    feeTransaction: str
    withdrawMin: str
    depositMin: str
    withdrawMax: str
    tokenAddress: str
    isToken: bool
    isMemo: bool
    memoRegex: str
    chainType: str
    confirmations: int
    amountUsable: str
    amountFrozen: str
    amountAll: str
    addressRegex: str
    label: str

QueryCoinsResult = NewType("QueryCoinsResult", List[Coin])

class QueryCoinByCodeParams(TypedDict):
    coinCode: str

class QueryCoinByCodeResult(Coin):
    pass

class Address(TypedDict):
    coinCode: str
    address: str
    memo: str

class QueryAddressesByCoinCodeParams(TypedDict):
    coinCode: str
    pageNum: int
    # pageSize: int

class QueryAddressesByCoinCodeResult(TypedDict):
    coinCode: str
    size: int
    total: int
    pageNum: int
    pageSize: int
    addressList: List[Address]

class QueryAddressesInfoParams(TypedDict):
    coinCode: str
    addressList: List[Address]

QueryAddressesInfoResult = NewType("QueryAddressesInfoResult", List[Address])

class CheckAddressParams(TypedDict):
    coinCode: str
    address: str
    memo: str

class CheckAddressResult(TypedDict):
    coinCode: str
    address: str
    memo: str
    status: int

class GetDepositAddressParams(TypedDict):
    coinCode: str

GetDepositAddressResult = NewType("GetDepositAddressResult", List[Address])

class WithdrawApplyParams(TypedDict):
    requestOrderId: str
    coinCode: str
    tokenAddress: str
    address: str
    memo: str
    amount: str
    timestamp: int

class WithdrawApplyResult(TypedDict):
    success: bool
    message: str
    requestOrderId: str
    coinCode: str
    address: str
    memo: str
    amount: str
    timestamp: int

class QueryByReqOrderIdParams(TypedDict):
    requestOrderId: str

class QueryByReqOrderIdResult:
    orderNumber: str
    externalOrderId: str
    orderType: str
    orderStatus: int
    description: str
    orderTimeStamp: str
    coinCode: str
    assetCode: str
    fromAddress: str
    toAddress: str
    amount: str
    memo: str
    transactionFee: str
    feeCoin: str
    orderFee: str
    transactionHash: str
    transactionStatus: int
    transactionType: str
    blockHeight: int
    blockHash: str
    chainCoin: str
    tokenAddress: str
    transactionIndex: str

class TransactionsParams(TypedDict):
    coinCode: str
    address: str
    beginTime: Optional[int]
    endTime: Optional[int]

class Transaction(TypedDict):
    custodyOrderId: str
    coinCode: str
    coinName: str
    coinName: str
    toAddress: str
    addressSourceType: str
    memo: str
    orderType: str
    orderStatus: int
    orderTimestamp: str
    endTime: int
    amount: str
    orderAmount: str
    feeCoin: str
    orderFee: str
    transactionHash: str
    blockHeight: str
    blockHash: str
    chainCoin: str
    tokenAddress: str
    timeStamp: int
    transactionStatus: int
    transactionIndex: str

TransactionsResult = NewType("TransactionsResult", List[Transaction])

class TransactionByIdParams(TypedDict):
    custodyOrderId: str
    orderType: str

class TransactionByIdResult(Transaction):
    pass

class TransactionByTxHashParams(TypedDict):
    coinCode: str
    txHash: str

class TransactionByTxHashResult(Transaction):
    pass

class TransactionByBlockHeightParams(TypedDict):
    coinCode: str
    blockHeight: str

TransactionByBlockHeightResult = NewType("TransactionByBlockHeightResult", List[Transaction])

class PendingTransaction(TypedDict):
    custodyOrderId: str
    coinCode: str
    coinName: str
    assetCode: str
    decimals: int
    toAddress: str
    addressSourceType: str
    memo: str
    orderType: str
    orderStatus: int
    orderTimestamp: str
    endTime: int
    amount: str
    orderAmount: str
    feeCoin: str
    orderFee: str
    transactionHash: str
    blockHeight: str
    blockHash: str
    chainCoin: str
    tokenAddress: str
    timeStamp: int
    transactionStatus: int
    transactionIndex: str
    confirmingThreshold: int
    confirmedNum: int

class PendingTransactionsParams(TypedDict):
    coinCode: Optional[str]
    address: Optional[str]
    beginTime: Optional[int]
    endTime: Optional[int]

PendingTransactionsResult = NewType("PendingTransactionsResult", List[PendingTransaction])

class PendingTransactionByIdParams(TypedDict):
    custodyOrderId: str
    orderType: str

class PendingTransactionByIdResult(PendingTransaction):
    pass

class BlockInfo(TypedDict):
    coinCode: str
    blockHeight: str
    chainCoin: str

class BlockHeightParams(TypedDict):
    chainCoin: Optional[str]

BlockHeightResult = NewType("BlockHeightResult", List[BlockInfo])

