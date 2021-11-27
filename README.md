# Invault OpenAPI Wrapped with python
More details about Invault OpenAPI are listed on [Invault OpenAPI documentation](https://github.com/invault-space/documentation-en).

## Examples
```py
import invaultapi

url = "http://localhost:8084/open/api/v1"
private_key = "YOUR-PEM-PRIVATE-KEY"
keyid = "YOUR-KEYID"
client = invaultapi.Client(url, private_key, keyid)
```
### queryAddressesByCoin
```py
import invaultapi.message as message


params = message.QueryAddressesByCoinCodeParams(coinCode = "BTC", pageNum = 0)
resp = client.assets.query_addresses_by_coin_code(params)
asset isinstance(resp, message.QueryAddressesByCoinCodeResult)
```
### blockHeight
```py
import invaultapi.message as message


params = message.BlockHeightParams(chainCoin = "BTC")
resp = client.transaction.block_height(params)
asset isinstance(resp, message.QueryAddressesByCoinCodeResult(list))
```
