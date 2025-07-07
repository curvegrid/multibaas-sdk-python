# multibaas_sdk.EventsApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_count**](EventsApi.md#get_event_count) | **GET** /events/count | Get event count
[**list_events**](EventsApi.md#list_events) | **GET** /events | List events


# **get_event_count**
> GetEventCount200Response get_event_count(block_hash=block_hash, block_number=block_number, tx_index_in_block=tx_index_in_block, event_index_in_log=event_index_in_log, tx_hash=tx_hash, from_constructor=from_constructor, chain=chain, contract_address=contract_address, contract_label=contract_label, event_signature=event_signature, limit=limit, offset=offset)

Get event count

Gets the number of events stored in the database.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.get_event_count200_response import GetEventCount200Response
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
    api_instance = multibaas_sdk.EventsApi(api_client)
    block_hash = 'block_hash_example' # str | Filter events by a block hash. (optional)
    block_number = 56 # int | Filter events by a block number. (optional)
    tx_index_in_block = 56 # int | Filter events by a transaction's index in the block. (optional)
    event_index_in_log = 56 # int | Filter events by index in the log. (optional)
    tx_hash = 'tx_hash_example' # str | Filter events by a transaction hash. (optional)
    from_constructor = True # bool | Filter events by whether they were emitted from the constructor function. (optional)
    chain = multibaas_sdk.ChainName() # ChainName | Filter events by a chain name. (optional)
    contract_address = 'contract_address_example' # str | Filter events by a contract address. (optional)
    contract_label = 'contract_label_example' # str | Filter events by a contract label. (optional)
    event_signature = 'event_signature_example' # str | Filter events by the signature. (optional)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # Get event count
        api_response = api_instance.get_event_count(block_hash=block_hash, block_number=block_number, tx_index_in_block=tx_index_in_block, event_index_in_log=event_index_in_log, tx_hash=tx_hash, from_constructor=from_constructor, chain=chain, contract_address=contract_address, contract_label=contract_label, event_signature=event_signature, limit=limit, offset=offset)
        print("The response of EventsApi->get_event_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| Filter events by a block hash. | [optional] 
 **block_number** | **int**| Filter events by a block number. | [optional] 
 **tx_index_in_block** | **int**| Filter events by a transaction&#39;s index in the block. | [optional] 
 **event_index_in_log** | **int**| Filter events by index in the log. | [optional] 
 **tx_hash** | **str**| Filter events by a transaction hash. | [optional] 
 **from_constructor** | **bool**| Filter events by whether they were emitted from the constructor function. | [optional] 
 **chain** | [**ChainName**](.md)| Filter events by a chain name. | [optional] 
 **contract_address** | **str**| Filter events by a contract address. | [optional] 
 **contract_label** | **str**| Filter events by a contract label. | [optional] 
 **event_signature** | **str**| Filter events by the signature. | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**GetEventCount200Response**](GetEventCount200Response.md)

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

# **list_events**
> ListEvents200Response list_events(block_hash=block_hash, block_number=block_number, tx_index_in_block=tx_index_in_block, event_index_in_log=event_index_in_log, tx_hash=tx_hash, from_constructor=from_constructor, chain=chain, contract_address=contract_address, contract_label=contract_label, event_signature=event_signature, limit=limit, offset=offset)

List events

Returns all events stored in the database.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.list_events200_response import ListEvents200Response
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
    api_instance = multibaas_sdk.EventsApi(api_client)
    block_hash = 'block_hash_example' # str | Filter events by a block hash. (optional)
    block_number = 56 # int | Filter events by a block number. (optional)
    tx_index_in_block = 56 # int | Filter events by a transaction's index in the block. (optional)
    event_index_in_log = 56 # int | Filter events by index in the log. (optional)
    tx_hash = 'tx_hash_example' # str | Filter events by a transaction hash. (optional)
    from_constructor = True # bool | Filter events by whether they were emitted from the constructor function. (optional)
    chain = multibaas_sdk.ChainName() # ChainName | Filter events by a chain name. (optional)
    contract_address = 'contract_address_example' # str | Filter events by a contract address. (optional)
    contract_label = 'contract_label_example' # str | Filter events by a contract label. (optional)
    event_signature = 'event_signature_example' # str | Filter events by the signature. (optional)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # List events
        api_response = api_instance.list_events(block_hash=block_hash, block_number=block_number, tx_index_in_block=tx_index_in_block, event_index_in_log=event_index_in_log, tx_hash=tx_hash, from_constructor=from_constructor, chain=chain, contract_address=contract_address, contract_label=contract_label, event_signature=event_signature, limit=limit, offset=offset)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| Filter events by a block hash. | [optional] 
 **block_number** | **int**| Filter events by a block number. | [optional] 
 **tx_index_in_block** | **int**| Filter events by a transaction&#39;s index in the block. | [optional] 
 **event_index_in_log** | **int**| Filter events by index in the log. | [optional] 
 **tx_hash** | **str**| Filter events by a transaction hash. | [optional] 
 **from_constructor** | **bool**| Filter events by whether they were emitted from the constructor function. | [optional] 
 **chain** | [**ChainName**](.md)| Filter events by a chain name. | [optional] 
 **contract_address** | **str**| Filter events by a contract address. | [optional] 
 **contract_label** | **str**| Filter events by a contract label. | [optional] 
 **event_signature** | **str**| Filter events by the signature. | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**ListEvents200Response**](ListEvents200Response.md)

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

