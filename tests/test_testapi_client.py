import warnings

import pytest

from helper.util import (
    get_method_fn,
    to_underline_name,
    upper_first_char,
)
import invaultapi.abi as abi
from invaultapi import Client


def call(url, rsa, keyid, methods, method_name):
    testapi_client = Client(url, rsa.private_key(), keyid)
    for m in methods:
        name = m["name"]
        if name != method_name:
            continue
        params = m["params"]
        method_fn_name = to_underline_name(name)
        method_fn = get_method_fn(testapi_client, method_fn_name)
        abi_name = upper_first_char(name)
        method_abi = getattr(abi, abi_name, None)
        try:
            method_fn(method_abi[1](**params))
        except RuntimeError as e:
            warnings.warn(str(e.args[0]), UserWarning)

def test_queryAssets(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryAssets")

def test_queryAssetByCode(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryAssetByCode")

@pytest.mark.timeout(3)
def test_queryCoins(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryCoins")

def test_queryCoinByCode(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryCoinByCode")

def test_queryAddressesByCoinCode(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryAddressesByCoinCode")

def test_queryAddressesInfo(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryAddressesByCoinCode")

def test_checkAddress(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "checkAddress")

def test_getDepositAddress(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "getDepositAddress")

def test_withdrawApply(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "withdrawApply")

def test_queryByReqOrderId(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "queryByReqOrderId")

def test_transactions(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "transactions")

def test_transactionById(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "transactionById")

def test_pendingTransactions(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "pendingTransactions")

def test_pendingTransactionById(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "pendingTransactionById")

def test_transactionByTxHash(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "transactionByTxHash")

def test_blockHeight(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "blockHeight")

def test_transactionByBlockHeight(testapi_url, rsa_key, keyid, api_mock_data):
    methods = api_mock_data["methods"]
    call(testapi_url, rsa_key, keyid, methods, "transactionByBlockHeight")

