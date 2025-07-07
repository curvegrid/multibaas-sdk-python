# multibaas_sdk.ChainsApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block**](ChainsApi.md#get_block) | **GET** /chains/{chain}/blocks/{block} | Get a block
[**get_chain_status**](ChainsApi.md#get_chain_status) | **GET** /chains/{chain}/status | Get chain status
[**get_transaction**](ChainsApi.md#get_transaction) | **GET** /chains/{chain}/transactions/{hash} | Get transaction
[**get_transaction_receipt**](ChainsApi.md#get_transaction_receipt) | **GET** /chains/{chain}/transactions/receipt/{hash} | Get transaction receipt
[**submit_signed_transaction**](ChainsApi.md#submit_signed_transaction) | **POST** /chains/{chain}/transactions/submit | Submit signed transaction
[**transfer_eth**](ChainsApi.md#transfer_eth) | **POST** /chains/{chain}/transfers | Transfer ETH


# **get_block**
> GetBlock200Response get_block(chain, block)

Get a block

Returns a block.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.get_block200_response import GetBlock200Response
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
    api_instance = multibaas_sdk.ChainsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    block = 'block_example' # str | A block number, hash or 'latest' for the latest block.

    try:
        # Get a block
        api_response = api_instance.get_block(chain, block)
        print("The response of ChainsApi->get_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChainsApi->get_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **block** | **str**| A block number, hash or &#39;latest&#39; for the latest block. | 

### Return type

[**GetBlock200Response**](GetBlock200Response.md)

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

# **get_chain_status**
> GetChainStatus200Response get_chain_status(chain)

Get chain status

Returns the chain status.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.get_chain_status200_response import GetChainStatus200Response
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
    api_instance = multibaas_sdk.ChainsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.

    try:
        # Get chain status
        api_response = api_instance.get_chain_status(chain)
        print("The response of ChainsApi->get_chain_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChainsApi->get_chain_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 

### Return type

[**GetChainStatus200Response**](GetChainStatus200Response.md)

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

# **get_transaction**
> GetTransaction200Response get_transaction(chain, hash, include=include)

Get transaction

Returns a transaction.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.get_transaction200_response import GetTransaction200Response
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
    api_instance = multibaas_sdk.ChainsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    hash = 'hash_example' # str | A transaction hash.
    include = 'include_example' # str | Include contract and method call details, if available. (optional)

    try:
        # Get transaction
        api_response = api_instance.get_transaction(chain, hash, include=include)
        print("The response of ChainsApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChainsApi->get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **hash** | **str**| A transaction hash. | 
 **include** | **str**| Include contract and method call details, if available. | [optional] 

### Return type

[**GetTransaction200Response**](GetTransaction200Response.md)

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

# **get_transaction_receipt**
> GetTransactionReceipt200Response get_transaction_receipt(chain, hash, include=include)

Get transaction receipt

Returns the receipt of a transaction that's been successfully added to the blockchain.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.get_transaction_receipt200_response import GetTransactionReceipt200Response
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
    api_instance = multibaas_sdk.ChainsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    hash = 'hash_example' # str | A transaction hash.
    include = 'include_example' # str | Include contract and event details, if available. (optional)

    try:
        # Get transaction receipt
        api_response = api_instance.get_transaction_receipt(chain, hash, include=include)
        print("The response of ChainsApi->get_transaction_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChainsApi->get_transaction_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **hash** | **str**| A transaction hash. | 
 **include** | **str**| Include contract and event details, if available. | [optional] 

### Return type

[**GetTransactionReceipt200Response**](GetTransactionReceipt200Response.md)

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

# **submit_signed_transaction**
> SubmitSignedTransaction200Response submit_signed_transaction(chain, signed_transaction_submission)

Submit signed transaction

Receives a pre-signed raw transaction and submits it to the blockchain.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.signed_transaction_submission import SignedTransactionSubmission
from multibaas_sdk.models.submit_signed_transaction200_response import SubmitSignedTransaction200Response
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
    api_instance = multibaas_sdk.ChainsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    signed_transaction_submission = multibaas_sdk.SignedTransactionSubmission() # SignedTransactionSubmission | 

    try:
        # Submit signed transaction
        api_response = api_instance.submit_signed_transaction(chain, signed_transaction_submission)
        print("The response of ChainsApi->submit_signed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChainsApi->submit_signed_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **signed_transaction_submission** | [**SignedTransactionSubmission**](SignedTransactionSubmission.md)|  | 

### Return type

[**SubmitSignedTransaction200Response**](SubmitSignedTransaction200Response.md)

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

# **transfer_eth**
> TransferEth200Response transfer_eth(chain, post_method_args)

Transfer ETH

Returns a transaction for sending the native token between addresses.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.post_method_args import PostMethodArgs
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
    api_instance = multibaas_sdk.ChainsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    post_method_args = multibaas_sdk.PostMethodArgs() # PostMethodArgs | 

    try:
        # Transfer ETH
        api_response = api_instance.transfer_eth(chain, post_method_args)
        print("The response of ChainsApi->transfer_eth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChainsApi->transfer_eth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **post_method_args** | [**PostMethodArgs**](PostMethodArgs.md)|  | 

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

