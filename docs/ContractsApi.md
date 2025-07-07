# multibaas_sdk.ContractsApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_contract_function**](ContractsApi.md#call_contract_function) | **POST** /chains/{chain}/addresses/{address-or-alias}/contracts/{contract}/methods/{method} | Call a contract function
[**create_contract**](ContractsApi.md#create_contract) | **POST** /contracts/{contract} | Create a contract
[**create_contracts**](ContractsApi.md#create_contracts) | **POST** /contracts | Create multiple contracts
[**delete_contract**](ContractsApi.md#delete_contract) | **DELETE** /contracts/{contract} | Delete a contract
[**delete_contract_version**](ContractsApi.md#delete_contract_version) | **DELETE** /contracts/{contract}/{version} | Delete a contract version
[**deploy_contract**](ContractsApi.md#deploy_contract) | **POST** /contracts/{contract}/deploy | Deploy a contract
[**deploy_contract_version**](ContractsApi.md#deploy_contract_version) | **POST** /contracts/{contract}/{version}/deploy | Deploy a contract version
[**get_contract**](ContractsApi.md#get_contract) | **GET** /contracts/{contract} | Get a contract
[**get_contract_version**](ContractsApi.md#get_contract_version) | **GET** /contracts/{contract}/{version} | Get a contract version
[**get_contract_versions**](ContractsApi.md#get_contract_versions) | **GET** /contracts/{contract}/all | Get all contract versions
[**get_event_monitor_status**](ContractsApi.md#get_event_monitor_status) | **GET** /chains/{chain}/addresses/{address-or-alias}/contracts/{contract}/status | Get event monitor status
[**get_event_type_conversions**](ContractsApi.md#get_event_type_conversions) | **GET** /contracts/{contract}/{version}/events/{event} | Get event type conversions
[**get_function_type_conversions**](ContractsApi.md#get_function_type_conversions) | **GET** /contracts/{contract}/{version}/methods/{method} | Get function type conversions
[**link_address_contract**](ContractsApi.md#link_address_contract) | **POST** /chains/{chain}/addresses/{address-or-alias}/contracts | Link address and contract
[**list_contract_versions**](ContractsApi.md#list_contract_versions) | **GET** /contracts/{contract}/versions | List all contract versions
[**list_contracts**](ContractsApi.md#list_contracts) | **GET** /contracts | List contracts
[**set_event_type_conversions**](ContractsApi.md#set_event_type_conversions) | **POST** /contracts/{contract}/{version}/events/{event} | Set event type conversions
[**set_function_type_conversions**](ContractsApi.md#set_function_type_conversions) | **POST** /contracts/{contract}/{version}/methods/{method} | Set function type conversions
[**unlink_address_contract**](ContractsApi.md#unlink_address_contract) | **DELETE** /chains/{chain}/addresses/{address-or-alias}/contracts/{contract} | Unlink address and contract


# **call_contract_function**
> CallContractFunction200Response call_contract_function(chain, address_or_alias, contract, method, post_method_args)

Call a contract function

Builds a transaction to call the given contract function. Returns a transaction to be signed and signs and submits to the blockchain it if the `signAndSubmit` flag is enabled.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.call_contract_function200_response import CallContractFunction200Response
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.post_method_args import PostMethodArgs
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    address_or_alias = 'address_or_alias_example' # str | An address or the alias of an address.
    contract = 'contract_example' # str | 
    method = 'method_example' # str | Contract function.
    post_method_args = multibaas_sdk.PostMethodArgs() # PostMethodArgs | 

    try:
        # Call a contract function
        api_response = api_instance.call_contract_function(chain, address_or_alias, contract, method, post_method_args)
        print("The response of ContractsApi->call_contract_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->call_contract_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **address_or_alias** | **str**| An address or the alias of an address. | 
 **contract** | **str**|  | 
 **method** | **str**| Contract function. | 
 **post_method_args** | [**PostMethodArgs**](PostMethodArgs.md)|  | 

### Return type

[**CallContractFunction200Response**](CallContractFunction200Response.md)

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

# **create_contract**
> GetContract200Response create_contract(contract, base_contract)

Create a contract

Adds a contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_contract import BaseContract
from multibaas_sdk.models.get_contract200_response import GetContract200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    base_contract = multibaas_sdk.BaseContract() # BaseContract | 

    try:
        # Create a contract
        api_response = api_instance.create_contract(contract, base_contract)
        print("The response of ContractsApi->create_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **base_contract** | [**BaseContract**](BaseContract.md)|  | 

### Return type

[**GetContract200Response**](GetContract200Response.md)

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

# **create_contracts**
> BaseResponse create_contracts(base_contract)

Create multiple contracts

Adds multiple contracts.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_contract import BaseContract
from multibaas_sdk.models.base_response import BaseResponse
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    base_contract = [multibaas_sdk.BaseContract()] # List[BaseContract] | 

    try:
        # Create multiple contracts
        api_response = api_instance.create_contracts(base_contract)
        print("The response of ContractsApi->create_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_contract** | [**List[BaseContract]**](BaseContract.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **delete_contract**
> BaseResponse delete_contract(contract)

Delete a contract

Deletes a contract and all its versions.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 

    try:
        # Delete a contract
        api_response = api_instance.delete_contract(contract)
        print("The response of ContractsApi->delete_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->delete_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **delete_contract_version**
> BaseResponse delete_contract_version(contract, version)

Delete a contract version

Deletes a specific contract version.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.

    try:
        # Delete a contract version
        api_response = api_instance.delete_contract_version(contract, version)
        print("The response of ContractsApi->delete_contract_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->delete_contract_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **deploy_contract**
> DeployContract200Response deploy_contract(contract, post_method_args)

Deploy a contract

Returns a transaction to deploy the given contract to the blockchain.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.deploy_contract200_response import DeployContract200Response
from multibaas_sdk.models.post_method_args import PostMethodArgs
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    post_method_args = multibaas_sdk.PostMethodArgs() # PostMethodArgs | 

    try:
        # Deploy a contract
        api_response = api_instance.deploy_contract(contract, post_method_args)
        print("The response of ContractsApi->deploy_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->deploy_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **post_method_args** | [**PostMethodArgs**](PostMethodArgs.md)|  | 

### Return type

[**DeployContract200Response**](DeployContract200Response.md)

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

# **deploy_contract_version**
> DeployContract200Response deploy_contract_version(contract, version, post_method_args)

Deploy a contract version

Returns a transaction to deploy the given contract version to the blockchain.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.deploy_contract200_response import DeployContract200Response
from multibaas_sdk.models.post_method_args import PostMethodArgs
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.
    post_method_args = multibaas_sdk.PostMethodArgs() # PostMethodArgs | 

    try:
        # Deploy a contract version
        api_response = api_instance.deploy_contract_version(contract, version, post_method_args)
        print("The response of ContractsApi->deploy_contract_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->deploy_contract_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 
 **post_method_args** | [**PostMethodArgs**](PostMethodArgs.md)|  | 

### Return type

[**DeployContract200Response**](DeployContract200Response.md)

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

# **get_contract**
> GetContract200Response get_contract(contract)

Get a contract

Returns the given contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_contract200_response import GetContract200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 

    try:
        # Get a contract
        api_response = api_instance.get_contract(contract)
        print("The response of ContractsApi->get_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 

### Return type

[**GetContract200Response**](GetContract200Response.md)

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

# **get_contract_version**
> GetContract200Response get_contract_version(contract, version)

Get a contract version

Returns a specific contract version.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_contract200_response import GetContract200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.

    try:
        # Get a contract version
        api_response = api_instance.get_contract_version(contract, version)
        print("The response of ContractsApi->get_contract_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 

### Return type

[**GetContract200Response**](GetContract200Response.md)

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

# **get_contract_versions**
> GetContractVersions200Response get_contract_versions(contract)

Get all contract versions

Returns all the versions of a contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_contract_versions200_response import GetContractVersions200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 

    try:
        # Get all contract versions
        api_response = api_instance.get_contract_versions(contract)
        print("The response of ContractsApi->get_contract_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 

### Return type

[**GetContractVersions200Response**](GetContractVersions200Response.md)

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

# **get_event_monitor_status**
> GetEventMonitorStatus200Response get_event_monitor_status(chain, address_or_alias, contract)

Get event monitor status

Returns the event monitor status for a given address and contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.get_event_monitor_status200_response import GetEventMonitorStatus200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    address_or_alias = 'address_or_alias_example' # str | An address or the alias of an address.
    contract = 'contract_example' # str | 

    try:
        # Get event monitor status
        api_response = api_instance.get_event_monitor_status(chain, address_or_alias, contract)
        print("The response of ContractsApi->get_event_monitor_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_event_monitor_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **address_or_alias** | **str**| An address or the alias of an address. | 
 **contract** | **str**|  | 

### Return type

[**GetEventMonitorStatus200Response**](GetEventMonitorStatus200Response.md)

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

# **get_event_type_conversions**
> GetEventTypeConversions200Response get_event_type_conversions(contract, version, event)

Get event type conversions

Returns the type conversion options for a given contract and event signature.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_event_type_conversions200_response import GetEventTypeConversions200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.
    event = 'event_example' # str | Contract Event.

    try:
        # Get event type conversions
        api_response = api_instance.get_event_type_conversions(contract, version, event)
        print("The response of ContractsApi->get_event_type_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_event_type_conversions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 
 **event** | **str**| Contract Event. | 

### Return type

[**GetEventTypeConversions200Response**](GetEventTypeConversions200Response.md)

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

# **get_function_type_conversions**
> GetFunctionTypeConversions200Response get_function_type_conversions(contract, version, method)

Get function type conversions

Returns the type conversion options for a given contract and function signature.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_function_type_conversions200_response import GetFunctionTypeConversions200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.
    method = 'method_example' # str | Contract function.

    try:
        # Get function type conversions
        api_response = api_instance.get_function_type_conversions(contract, version, method)
        print("The response of ContractsApi->get_function_type_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_function_type_conversions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 
 **method** | **str**| Contract function. | 

### Return type

[**GetFunctionTypeConversions200Response**](GetFunctionTypeConversions200Response.md)

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

# **link_address_contract**
> SetAddress201Response link_address_contract(chain, address_or_alias, link_address_contract_request)

Link address and contract

Links an address to a contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.link_address_contract_request import LinkAddressContractRequest
from multibaas_sdk.models.set_address201_response import SetAddress201Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    address_or_alias = 'address_or_alias_example' # str | An address or the alias of an address.
    link_address_contract_request = multibaas_sdk.LinkAddressContractRequest() # LinkAddressContractRequest | 

    try:
        # Link address and contract
        api_response = api_instance.link_address_contract(chain, address_or_alias, link_address_contract_request)
        print("The response of ContractsApi->link_address_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->link_address_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **address_or_alias** | **str**| An address or the alias of an address. | 
 **link_address_contract_request** | [**LinkAddressContractRequest**](LinkAddressContractRequest.md)|  | 

### Return type

[**SetAddress201Response**](SetAddress201Response.md)

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

# **list_contract_versions**
> ListContractVersions200Response list_contract_versions(contract)

List all contract versions

Returns a list of the versions of a contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_contract_versions200_response import ListContractVersions200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 

    try:
        # List all contract versions
        api_response = api_instance.list_contract_versions(contract)
        print("The response of ContractsApi->list_contract_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->list_contract_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 

### Return type

[**ListContractVersions200Response**](ListContractVersions200Response.md)

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

# **list_contracts**
> ListContracts200Response list_contracts()

List contracts

Returns a list of contracts.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_contracts200_response import ListContracts200Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)

    try:
        # List contracts
        api_response = api_instance.list_contracts()
        print("The response of ContractsApi->list_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->list_contracts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListContracts200Response**](ListContracts200Response.md)

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

# **set_event_type_conversions**
> BaseResponse set_event_type_conversions(contract, version, event, contract_event_options)

Set event type conversions

Sets the type conversion options for a given contract and event signature.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.contract_event_options import ContractEventOptions
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.
    event = 'event_example' # str | Contract Event.
    contract_event_options = multibaas_sdk.ContractEventOptions() # ContractEventOptions | 

    try:
        # Set event type conversions
        api_response = api_instance.set_event_type_conversions(contract, version, event, contract_event_options)
        print("The response of ContractsApi->set_event_type_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->set_event_type_conversions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 
 **event** | **str**| Contract Event. | 
 **contract_event_options** | [**ContractEventOptions**](ContractEventOptions.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **set_function_type_conversions**
> BaseResponse set_function_type_conversions(contract, version, method, contract_method_options)

Set function type conversions

Sets the type conversion options for a given contract and function signature.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.contract_method_options import ContractMethodOptions
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    contract = 'contract_example' # str | 
    version = 'version_example' # str | Contract Version.
    method = 'method_example' # str | Contract function.
    contract_method_options = multibaas_sdk.ContractMethodOptions() # ContractMethodOptions | 

    try:
        # Set function type conversions
        api_response = api_instance.set_function_type_conversions(contract, version, method, contract_method_options)
        print("The response of ContractsApi->set_function_type_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->set_function_type_conversions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **version** | **str**| Contract Version. | 
 **method** | **str**| Contract function. | 
 **contract_method_options** | [**ContractMethodOptions**](ContractMethodOptions.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **unlink_address_contract**
> SetAddress201Response unlink_address_contract(chain, address_or_alias, contract)

Unlink address and contract

Unlinks an address from a contract.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.set_address201_response import SetAddress201Response
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
    api_instance = multibaas_sdk.ContractsApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    address_or_alias = 'address_or_alias_example' # str | An address or the alias of an address.
    contract = 'contract_example' # str | 

    try:
        # Unlink address and contract
        api_response = api_instance.unlink_address_contract(chain, address_or_alias, contract)
        print("The response of ContractsApi->unlink_address_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->unlink_address_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **address_or_alias** | **str**| An address or the alias of an address. | 
 **contract** | **str**|  | 

### Return type

[**SetAddress201Response**](SetAddress201Response.md)

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

