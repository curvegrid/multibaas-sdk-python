# multibaas_sdk.TxmApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_transaction**](TxmApi.md#cancel_transaction) | **POST** /chains/{chain}/txm/{wallet_address}/nonce/{nonce}/cancel | Cancel transaction
[**count_wallet_transactions**](TxmApi.md#count_wallet_transactions) | **GET** /chains/{chain}/txm/{wallet_address}/count | Count all transactions for a wallet
[**list_wallet_transactions**](TxmApi.md#list_wallet_transactions) | **GET** /chains/{chain}/txm/{wallet_address} | List transactions for a wallet
[**speed_up_transaction**](TxmApi.md#speed_up_transaction) | **POST** /chains/{chain}/txm/{wallet_address}/nonce/{nonce}/speed_up | Speed up transaction


# **cancel_transaction**
> TransferEth200Response cancel_transaction(chain, wallet_address, nonce, gas_params)

Cancel transaction

Cancels a transaction by resubmitting it as no-op transaction and with a higher gas price.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.gas_params import GasParams
from multibaas_sdk.models.transfer_eth200_response import TransferEth200Response
from multibaas_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your_deployment.multibaas.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = multibaas_sdk.Configuration(
    host = "https://your_deployment.multibaas.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = multibaas_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.TxmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    wallet_address = 'wallet_address_example' # str | An Ethereum address.
    nonce = 56 # int | Transaction nonce.
    gas_params = multibaas_sdk.GasParams() # GasParams | 

    try:
        # Cancel transaction
        api_response = api_instance.cancel_transaction(chain, wallet_address, nonce, gas_params)
        print("The response of TxmApi->cancel_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TxmApi->cancel_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **wallet_address** | **str**| An Ethereum address. | 
 **nonce** | **int**| Transaction nonce. | 
 **gas_params** | [**GasParams**](GasParams.md)|  | 

### Return type

[**TransferEth200Response**](TransferEth200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error. |  -  |
**5XX** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_wallet_transactions**
> CountWalletTransactions200Response count_wallet_transactions(chain, wallet_address)

Count all transactions for a wallet

Count all transactions for the given wallet address.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.count_wallet_transactions200_response import CountWalletTransactions200Response
from multibaas_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your_deployment.multibaas.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = multibaas_sdk.Configuration(
    host = "https://your_deployment.multibaas.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = multibaas_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.TxmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    wallet_address = 'wallet_address_example' # str | An Ethereum address.

    try:
        # Count all transactions for a wallet
        api_response = api_instance.count_wallet_transactions(chain, wallet_address)
        print("The response of TxmApi->count_wallet_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TxmApi->count_wallet_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **wallet_address** | **str**| An Ethereum address. | 

### Return type

[**CountWalletTransactions200Response**](CountWalletTransactions200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error. |  -  |
**5XX** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wallet_transactions**
> ListWalletTransactions200Response list_wallet_transactions(chain, wallet_address, hash=hash, nonce=nonce, status=status, limit=limit, offset=offset)

List transactions for a wallet

List the transactions submitted by the given wallet address.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.list_wallet_transactions200_response import ListWalletTransactions200Response
from multibaas_sdk.models.transaction_status import TransactionStatus
from multibaas_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your_deployment.multibaas.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = multibaas_sdk.Configuration(
    host = "https://your_deployment.multibaas.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = multibaas_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.TxmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    wallet_address = 'wallet_address_example' # str | An Ethereum address.
    hash = 'hash_example' # str | Filter transactions by transaction hash. To filter for multiple hashes, use ampersands: `?hash=HASH1&hash=HASH2&hash=HASH3` (optional)
    nonce = 56 # int | Filter transactions by nonce (optional)
    status = multibaas_sdk.TransactionStatus() # TransactionStatus | Filter transactions by status (optional)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # List transactions for a wallet
        api_response = api_instance.list_wallet_transactions(chain, wallet_address, hash=hash, nonce=nonce, status=status, limit=limit, offset=offset)
        print("The response of TxmApi->list_wallet_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TxmApi->list_wallet_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **wallet_address** | **str**| An Ethereum address. | 
 **hash** | **str**| Filter transactions by transaction hash. To filter for multiple hashes, use ampersands: &#x60;?hash&#x3D;HASH1&amp;hash&#x3D;HASH2&amp;hash&#x3D;HASH3&#x60; | [optional] 
 **nonce** | **int**| Filter transactions by nonce | [optional] 
 **status** | [**TransactionStatus**](.md)| Filter transactions by status | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**ListWalletTransactions200Response**](ListWalletTransactions200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error. |  -  |
**5XX** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speed_up_transaction**
> TransferEth200Response speed_up_transaction(chain, wallet_address, nonce, gas_params)

Speed up transaction

Speeds up a transaction by resubmitting it with a higher gas price.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.gas_params import GasParams
from multibaas_sdk.models.transfer_eth200_response import TransferEth200Response
from multibaas_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your_deployment.multibaas.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = multibaas_sdk.Configuration(
    host = "https://your_deployment.multibaas.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = multibaas_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.TxmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    wallet_address = 'wallet_address_example' # str | An Ethereum address.
    nonce = 56 # int | Transaction nonce.
    gas_params = multibaas_sdk.GasParams() # GasParams | 

    try:
        # Speed up transaction
        api_response = api_instance.speed_up_transaction(chain, wallet_address, nonce, gas_params)
        print("The response of TxmApi->speed_up_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TxmApi->speed_up_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **wallet_address** | **str**| An Ethereum address. | 
 **nonce** | **int**| Transaction nonce. | 
 **gas_params** | [**GasParams**](GasParams.md)|  | 

### Return type

[**TransferEth200Response**](TransferEth200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error. |  -  |
**5XX** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

