# multibaas_sdk.HsmApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hsm_config**](HsmApi.md#add_hsm_config) | **POST** /hsm/config | Add HSM config
[**add_hsm_key**](HsmApi.md#add_hsm_key) | **POST** /hsm/key | Add HSM key
[**create_hsm_key**](HsmApi.md#create_hsm_key) | **POST** /hsm/key/new | Create HSM key
[**list_hsm**](HsmApi.md#list_hsm) | **GET** /hsm | List HSM configs and wallets
[**list_hsm_wallets**](HsmApi.md#list_hsm_wallets) | **GET** /hsm/wallets | List HSM wallets
[**remove_hsm_config**](HsmApi.md#remove_hsm_config) | **DELETE** /hsm/config/{client_id} | Remove HSM config
[**remove_hsm_key**](HsmApi.md#remove_hsm_key) | **DELETE** /hsm/key/{wallet_address} | Remove HSM key
[**set_local_nonce**](HsmApi.md#set_local_nonce) | **POST** /chains/{chain}/hsm/nonce/{wallet_address} | Set local nonce
[**sign_and_submit_transaction**](HsmApi.md#sign_and_submit_transaction) | **POST** /chains/{chain}/hsm/submit | Sign and submit transaction
[**sign_data**](HsmApi.md#sign_data) | **POST** /chains/{chain}/hsm/sign | Sign data


# **add_hsm_config**
> BaseResponse add_hsm_config(base_azure_account)

Add HSM config

Adds a new Azure account configuration.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_azure_account import BaseAzureAccount
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    base_azure_account = multibaas_sdk.BaseAzureAccount() # BaseAzureAccount | 

    try:
        # Add HSM config
        api_response = api_instance.add_hsm_config(base_azure_account)
        print("The response of HsmApi->add_hsm_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->add_hsm_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_azure_account** | [**BaseAzureAccount**](BaseAzureAccount.md)|  | 

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

# **add_hsm_key**
> BaseResponse add_hsm_key(add_key)

Add HSM key

Adds an existing key configuration.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.add_key import AddKey
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    add_key = multibaas_sdk.AddKey() # AddKey | 

    try:
        # Add HSM key
        api_response = api_instance.add_hsm_key(add_key)
        print("The response of HsmApi->add_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->add_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_key** | [**AddKey**](AddKey.md)|  | 

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

# **create_hsm_key**
> CreateHsmKey200Response create_hsm_key(create_key)

Create HSM key

Creates a new key in the Azure KeyVault.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.create_hsm_key200_response import CreateHsmKey200Response
from multibaas_sdk.models.create_key import CreateKey
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    create_key = multibaas_sdk.CreateKey() # CreateKey | 

    try:
        # Create HSM key
        api_response = api_instance.create_hsm_key(create_key)
        print("The response of HsmApi->create_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->create_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_key** | [**CreateKey**](CreateKey.md)|  | 

### Return type

[**CreateHsmKey200Response**](CreateHsmKey200Response.md)

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

# **list_hsm**
> ListHsm200Response list_hsm()

List HSM configs and wallets

Returns a list of HSM configs and their associated wallets.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_hsm200_response import ListHsm200Response
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
    api_instance = multibaas_sdk.HsmApi(api_client)

    try:
        # List HSM configs and wallets
        api_response = api_instance.list_hsm()
        print("The response of HsmApi->list_hsm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->list_hsm: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListHsm200Response**](ListHsm200Response.md)

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

# **list_hsm_wallets**
> ListHsmWallets200Response list_hsm_wallets(key_name=key_name, key_version=key_version, vault_name=vault_name, base_group_name=base_group_name, client_id=client_id, public_address=public_address, limit=limit, offset=offset)

List HSM wallets

Returns a list of HSM wallets.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_hsm_wallets200_response import ListHsmWallets200Response
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    key_name = 'key_name_example' # str | Filter wallets by a key name. (optional)
    key_version = 'key_version_example' # str | Filter wallets by a key version. (optional)
    vault_name = 'vault_name_example' # str | Filter wallets by a vault name. (optional)
    base_group_name = 'base_group_name_example' # str | Filter wallets by a base group name. (optional)
    client_id = 'client_id_example' # str | Filter wallets by a client ID. (optional)
    public_address = 'public_address_example' # str | Filter wallets by a public address. (optional)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # List HSM wallets
        api_response = api_instance.list_hsm_wallets(key_name=key_name, key_version=key_version, vault_name=vault_name, base_group_name=base_group_name, client_id=client_id, public_address=public_address, limit=limit, offset=offset)
        print("The response of HsmApi->list_hsm_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->list_hsm_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Filter wallets by a key name. | [optional] 
 **key_version** | **str**| Filter wallets by a key version. | [optional] 
 **vault_name** | **str**| Filter wallets by a vault name. | [optional] 
 **base_group_name** | **str**| Filter wallets by a base group name. | [optional] 
 **client_id** | **str**| Filter wallets by a client ID. | [optional] 
 **public_address** | **str**| Filter wallets by a public address. | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**ListHsmWallets200Response**](ListHsmWallets200Response.md)

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

# **remove_hsm_config**
> BaseResponse remove_hsm_config(client_id)

Remove HSM config

Removes the specified Azure account configuration and its associated keys.

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
    api_instance = multibaas_sdk.HsmApi(api_client)
    client_id = 'client_id_example' # str | The HSM client ID.

    try:
        # Remove HSM config
        api_response = api_instance.remove_hsm_config(client_id)
        print("The response of HsmApi->remove_hsm_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->remove_hsm_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The HSM client ID. | 

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

# **remove_hsm_key**
> BaseResponse remove_hsm_key(wallet_address)

Remove HSM key

Removes the specified key configuration.

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
    api_instance = multibaas_sdk.HsmApi(api_client)
    wallet_address = 'wallet_address_example' # str | An Ethereum address.

    try:
        # Remove HSM key
        api_response = api_instance.remove_hsm_key(wallet_address)
        print("The response of HsmApi->remove_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->remove_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_address** | **str**| An Ethereum address. | 

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

# **set_local_nonce**
> BaseResponse set_local_nonce(chain, wallet_address, set_nonce_request)

Set local nonce

Sets the next transaction nonce for the given HSM address that will be used with the nonce management feature.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.set_nonce_request import SetNonceRequest
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    wallet_address = 'wallet_address_example' # str | An Ethereum address.
    set_nonce_request = multibaas_sdk.SetNonceRequest() # SetNonceRequest | 

    try:
        # Set local nonce
        api_response = api_instance.set_local_nonce(chain, wallet_address, set_nonce_request)
        print("The response of HsmApi->set_local_nonce:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->set_local_nonce: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **wallet_address** | **str**| An Ethereum address. | 
 **set_nonce_request** | [**SetNonceRequest**](SetNonceRequest.md)|  | 

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

# **sign_and_submit_transaction**
> TransferEth200Response sign_and_submit_transaction(chain, cloud_wallet_txto_sign)

Sign and submit transaction

Signs and submits the given transaction using an HSM address.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.cloud_wallet_txto_sign import CloudWalletTXToSign
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    cloud_wallet_txto_sign = multibaas_sdk.CloudWalletTXToSign() # CloudWalletTXToSign | 

    try:
        # Sign and submit transaction
        api_response = api_instance.sign_and_submit_transaction(chain, cloud_wallet_txto_sign)
        print("The response of HsmApi->sign_and_submit_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->sign_and_submit_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **cloud_wallet_txto_sign** | [**CloudWalletTXToSign**](CloudWalletTXToSign.md)|  | 

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

# **sign_data**
> SignData200Response sign_data(chain, hsm_sign_request)

Sign data

Signs the given data using the given HSM address.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.chain_name import ChainName
from multibaas_sdk.models.hsm_sign_request import HSMSignRequest
from multibaas_sdk.models.sign_data200_response import SignData200Response
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
    api_instance = multibaas_sdk.HsmApi(api_client)
    chain = multibaas_sdk.ChainName() # ChainName | The blockchain chain label.
    hsm_sign_request = multibaas_sdk.HSMSignRequest() # HSMSignRequest | 

    try:
        # Sign data
        api_response = api_instance.sign_data(chain, hsm_sign_request)
        print("The response of HsmApi->sign_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HsmApi->sign_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | [**ChainName**](.md)| The blockchain chain label. | 
 **hsm_sign_request** | [**HSMSignRequest**](HSMSignRequest.md)|  | 

### Return type

[**SignData200Response**](SignData200Response.md)

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

