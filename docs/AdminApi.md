# multibaas_sdk.AdminApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invite**](AdminApi.md#accept_invite) | **POST** /invites/{inviteID} | Accept invite
[**add_cors_origin**](AdminApi.md#add_cors_origin) | **POST** /cors | Add CORS origin
[**add_group_api_key**](AdminApi.md#add_group_api_key) | **PUT** /groups/{groupID}/api_keys/{apiKeyID} | Add API key to group
[**add_group_role**](AdminApi.md#add_group_role) | **PUT** /groups/{groupID}/roles/{roleShortName} | Add role to group
[**add_group_user**](AdminApi.md#add_group_user) | **PUT** /groups/{groupID}/users/{userID} | Add user to group
[**check_invite**](AdminApi.md#check_invite) | **GET** /invites/{inviteID} | Check invite
[**create_api_key**](AdminApi.md#create_api_key) | **POST** /api_keys | Create API key
[**delete_api_key**](AdminApi.md#delete_api_key) | **DELETE** /api_keys/{apiKeyID} | Delete API key
[**delete_invite**](AdminApi.md#delete_invite) | **DELETE** /invites/{email}/delete | Delete invite
[**delete_user**](AdminApi.md#delete_user) | **DELETE** /users/{userID} | Delete user
[**get_api_key**](AdminApi.md#get_api_key) | **GET** /api_keys/{apiKeyID} | Get API Key
[**get_plan**](AdminApi.md#get_plan) | **GET** /plan | Get plan
[**invite_user**](AdminApi.md#invite_user) | **POST** /invites | Invite user
[**list_api_keys**](AdminApi.md#list_api_keys) | **GET** /api_keys | List API keys
[**list_audit_logs**](AdminApi.md#list_audit_logs) | **GET** /systemactivities | List audit logs
[**list_cors_origins**](AdminApi.md#list_cors_origins) | **GET** /cors | List CORS origins
[**list_groups**](AdminApi.md#list_groups) | **GET** /groups | List groups
[**list_invites**](AdminApi.md#list_invites) | **GET** /invites | List invites
[**list_user_signers**](AdminApi.md#list_user_signers) | **GET** /users/{userID}/signers | List user signers
[**list_users**](AdminApi.md#list_users) | **GET** /users | List users
[**remove_cors_origin**](AdminApi.md#remove_cors_origin) | **DELETE** /cors/{originID} | Remove CORS Origin
[**remove_group_api_key**](AdminApi.md#remove_group_api_key) | **DELETE** /groups/{groupID}/api_keys/{apiKeyID} | Remove API key from group
[**remove_group_role**](AdminApi.md#remove_group_role) | **DELETE** /groups/{groupID}/roles/{roleShortName} | Remove role from group
[**remove_group_user**](AdminApi.md#remove_group_user) | **DELETE** /groups/{groupID}/users/{userID} | Remove user from group
[**remove_user_signer_cloud_wallet**](AdminApi.md#remove_user_signer_cloud_wallet) | **DELETE** /users/{userID}/cloudwallets/{wallet_address} | Remove user cloud wallet signer
[**remove_user_signer_safe_account**](AdminApi.md#remove_user_signer_safe_account) | **DELETE** /users/{userID}/safeaccounts/{wallet_address} | Remove user safe account signer
[**remove_user_signer_web3_wallet**](AdminApi.md#remove_user_signer_web3_wallet) | **DELETE** /users/{userID}/web3wallets/{wallet_address} | Remove user web3 wallet signer
[**set_user_signer_cloud_wallet**](AdminApi.md#set_user_signer_cloud_wallet) | **PUT** /users/{userID}/cloudwallets/{wallet_address} | Add or update user cloud wallet signer
[**set_user_signer_safe_account**](AdminApi.md#set_user_signer_safe_account) | **PUT** /users/{userID}/safeaccounts/{wallet_address} | Add or update user safe account signer
[**set_user_signer_web3_wallet**](AdminApi.md#set_user_signer_web3_wallet) | **PUT** /users/{userID}/web3wallets/{wallet_address} | Add or update user web3 wallet signer
[**update_api_key**](AdminApi.md#update_api_key) | **PUT** /api_keys/{apiKeyID} | Update API key


# **accept_invite**
> AcceptInvite200Response accept_invite(invite_id, accept_invite_request)

Accept invite

Accepts a user invite.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.accept_invite200_response import AcceptInvite200Response
from multibaas_sdk.models.accept_invite_request import AcceptInviteRequest
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

# Configure Bearer authorization (JWT): bearer
configuration = multibaas_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.AdminApi(api_client)
    invite_id = 'invite_id_example' # str | 
    accept_invite_request = multibaas_sdk.AcceptInviteRequest() # AcceptInviteRequest | 

    try:
        # Accept invite
        api_response = api_instance.accept_invite(invite_id, accept_invite_request)
        print("The response of AdminApi->accept_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->accept_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **accept_invite_request** | [**AcceptInviteRequest**](AcceptInviteRequest.md)|  | 

### Return type

[**AcceptInvite200Response**](AcceptInvite200Response.md)

### Authorization

[bearer](../README.md#bearer)

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

# **add_cors_origin**
> BaseResponse add_cors_origin(cors_origin)

Add CORS origin

Adds a CORS origin.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.cors_origin import CORSOrigin
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    cors_origin = multibaas_sdk.CORSOrigin() # CORSOrigin | 

    try:
        # Add CORS origin
        api_response = api_instance.add_cors_origin(cors_origin)
        print("The response of AdminApi->add_cors_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->add_cors_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cors_origin** | [**CORSOrigin**](CORSOrigin.md)|  | 

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

# **add_group_api_key**
> BaseResponse add_group_api_key(group_id, api_key_id)

Add API key to group

Adds an API key to a group.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int | 
    api_key_id = 56 # int | 

    try:
        # Add API key to group
        api_response = api_instance.add_group_api_key(group_id, api_key_id)
        print("The response of AdminApi->add_group_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->add_group_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **api_key_id** | **int**|  | 

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

# **add_group_role**
> BaseResponse add_group_role(group_id, role_short_name)

Add role to group

Adds a role to a group.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int | 
    role_short_name = 'role_short_name_example' # str | 

    try:
        # Add role to group
        api_response = api_instance.add_group_role(group_id, role_short_name)
        print("The response of AdminApi->add_group_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->add_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **role_short_name** | **str**|  | 

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

# **add_group_user**
> BaseResponse add_group_user(group_id, user_id)

Add user to group

Adds a user to a group.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int | 
    user_id = 56 # int | 

    try:
        # Add user to group
        api_response = api_instance.add_group_user(group_id, user_id)
        print("The response of AdminApi->add_group_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->add_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **user_id** | **int**|  | 

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

# **check_invite**
> BaseResponse check_invite(invite_id)

Check invite

Checks if a user invite is valid.

### Example


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


# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.AdminApi(api_client)
    invite_id = 'invite_id_example' # str | 

    try:
        # Check invite
        api_response = api_instance.check_invite(invite_id)
        print("The response of AdminApi->check_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->check_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

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

# **create_api_key**
> CreateApiKey200Response create_api_key(create_api_key_request)

Create API key

Creates an API key and adds it to group IDs.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.create_api_key200_response import CreateApiKey200Response
from multibaas_sdk.models.create_api_key_request import CreateApiKeyRequest
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    create_api_key_request = multibaas_sdk.CreateApiKeyRequest() # CreateApiKeyRequest | 

    try:
        # Create API key
        api_response = api_instance.create_api_key(create_api_key_request)
        print("The response of AdminApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 

### Return type

[**CreateApiKey200Response**](CreateApiKey200Response.md)

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

# **delete_api_key**
> BaseResponse delete_api_key(api_key_id)

Delete API key

Deletes an API key.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    api_key_id = 56 # int | 

    try:
        # Delete API key
        api_response = api_instance.delete_api_key(api_key_id)
        print("The response of AdminApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**|  | 

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

# **delete_invite**
> delete_invite(email)

Delete invite

Deletes a user invite.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
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

# Configure Bearer authorization (JWT): bearer
configuration = multibaas_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with multibaas_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multibaas_sdk.AdminApi(api_client)
    email = 'email_example' # str | 

    try:
        # Delete invite
        api_instance.delete_invite(email)
    except Exception as e:
        print("Exception when calling AdminApi->delete_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**4XX** | Client error. |  -  |
**5XX** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> BaseResponse delete_user(user_id)

Delete user

Deletes a user.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 

    try:
        # Delete user
        api_response = api_instance.delete_user(user_id)
        print("The response of AdminApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

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

# **get_api_key**
> GetApiKey200Response get_api_key(api_key_id)

Get API Key

Returns an API key.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_api_key200_response import GetApiKey200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    api_key_id = 56 # int | 

    try:
        # Get API Key
        api_response = api_instance.get_api_key(api_key_id)
        print("The response of AdminApi->get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**|  | 

### Return type

[**GetApiKey200Response**](GetApiKey200Response.md)

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

# **get_plan**
> GetPlan200Response get_plan()

Get plan

Returns the current plan with limits and features.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_plan200_response import GetPlan200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)

    try:
        # Get plan
        api_response = api_instance.get_plan()
        print("The response of AdminApi->get_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_plan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPlan200Response**](GetPlan200Response.md)

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

# **invite_user**
> BaseResponse invite_user(invite_request)

Invite user

Invites a new user.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.invite_request import InviteRequest
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    invite_request = multibaas_sdk.InviteRequest() # InviteRequest | 

    try:
        # Invite user
        api_response = api_instance.invite_user(invite_request)
        print("The response of AdminApi->invite_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->invite_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_request** | [**InviteRequest**](InviteRequest.md)|  | 

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

# **list_api_keys**
> ListApiKeys200Response list_api_keys(all=all)

List API keys

Returns all the API keys.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_api_keys200_response import ListApiKeys200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    all = True # bool | If true, returns all API keys on the system, otherwise, returns only the API keys owned by the calling user. (optional)

    try:
        # List API keys
        api_response = api_instance.list_api_keys(all=all)
        print("The response of AdminApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| If true, returns all API keys on the system, otherwise, returns only the API keys owned by the calling user. | [optional] 

### Return type

[**ListApiKeys200Response**](ListApiKeys200Response.md)

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

# **list_audit_logs**
> ListAuditLogs200Response list_audit_logs()

List audit logs

Returns the audit logs.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_audit_logs200_response import ListAuditLogs200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)

    try:
        # List audit logs
        api_response = api_instance.list_audit_logs()
        print("The response of AdminApi->list_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_audit_logs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAuditLogs200Response**](ListAuditLogs200Response.md)

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

# **list_cors_origins**
> ListCorsOrigins200Response list_cors_origins()

List CORS origins

Returns a list of CORS origins.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_cors_origins200_response import ListCorsOrigins200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)

    try:
        # List CORS origins
        api_response = api_instance.list_cors_origins()
        print("The response of AdminApi->list_cors_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_cors_origins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListCorsOrigins200Response**](ListCorsOrigins200Response.md)

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

# **list_groups**
> ListGroups200Response list_groups(user_id=user_id, api_key_id=api_key_id, assignable=assignable)

List groups

Returns all the groups.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_groups200_response import ListGroups200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int |  (optional)
    api_key_id = 56 # int |  (optional)
    assignable = True # bool |  (optional)

    try:
        # List groups
        api_response = api_instance.list_groups(user_id=user_id, api_key_id=api_key_id, assignable=assignable)
        print("The response of AdminApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | [optional] 
 **api_key_id** | **int**|  | [optional] 
 **assignable** | **bool**|  | [optional] 

### Return type

[**ListGroups200Response**](ListGroups200Response.md)

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

# **list_invites**
> ListInvites200Response list_invites()

List invites

Returns all the user invites.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_invites200_response import ListInvites200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)

    try:
        # List invites
        api_response = api_instance.list_invites()
        print("The response of AdminApi->list_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_invites: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListInvites200Response**](ListInvites200Response.md)

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

# **list_user_signers**
> ListUserSigners200Response list_user_signers(user_id)

List user signers

Returns all the signers for a user.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_user_signers200_response import ListUserSigners200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 

    try:
        # List user signers
        api_response = api_instance.list_user_signers(user_id)
        print("The response of AdminApi->list_user_signers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_user_signers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**ListUserSigners200Response**](ListUserSigners200Response.md)

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

# **list_users**
> ListUsers200Response list_users(group_id=group_id)

List users

Returns all the users.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_users200_response import ListUsers200Response
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int |  (optional)

    try:
        # List users
        api_response = api_instance.list_users(group_id=group_id)
        print("The response of AdminApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | [optional] 

### Return type

[**ListUsers200Response**](ListUsers200Response.md)

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

# **remove_cors_origin**
> BaseResponse remove_cors_origin(origin_id)

Remove CORS Origin

Removes a CORS origin.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    origin_id = 56 # int | 

    try:
        # Remove CORS Origin
        api_response = api_instance.remove_cors_origin(origin_id)
        print("The response of AdminApi->remove_cors_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_cors_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_id** | **int**|  | 

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

# **remove_group_api_key**
> BaseResponse remove_group_api_key(group_id, api_key_id)

Remove API key from group

Removes an API key from a group.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int | 
    api_key_id = 56 # int | 

    try:
        # Remove API key from group
        api_response = api_instance.remove_group_api_key(group_id, api_key_id)
        print("The response of AdminApi->remove_group_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_group_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **api_key_id** | **int**|  | 

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

# **remove_group_role**
> BaseResponse remove_group_role(group_id, role_short_name)

Remove role from group

Removes a role from a group.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int | 
    role_short_name = 'role_short_name_example' # str | 

    try:
        # Remove role from group
        api_response = api_instance.remove_group_role(group_id, role_short_name)
        print("The response of AdminApi->remove_group_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **role_short_name** | **str**|  | 

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

# **remove_group_user**
> BaseResponse remove_group_user(group_id, user_id)

Remove user from group

Removes a user from a group.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    group_id = 56 # int | 
    user_id = 56 # int | 

    try:
        # Remove user from group
        api_response = api_instance.remove_group_user(group_id, user_id)
        print("The response of AdminApi->remove_group_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **user_id** | **int**|  | 

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

# **remove_user_signer_cloud_wallet**
> BaseResponse remove_user_signer_cloud_wallet(user_id, wallet_address)

Remove user cloud wallet signer

Removes a cloud wallet signer from a user.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 
    wallet_address = 'wallet_address_example' # str | An Ethereum address.

    try:
        # Remove user cloud wallet signer
        api_response = api_instance.remove_user_signer_cloud_wallet(user_id, wallet_address)
        print("The response of AdminApi->remove_user_signer_cloud_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_user_signer_cloud_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
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

# **remove_user_signer_safe_account**
> BaseResponse remove_user_signer_safe_account(user_id, wallet_address)

Remove user safe account signer

Removes a safe account signer from a user.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 
    wallet_address = 'wallet_address_example' # str | An Ethereum address.

    try:
        # Remove user safe account signer
        api_response = api_instance.remove_user_signer_safe_account(user_id, wallet_address)
        print("The response of AdminApi->remove_user_signer_safe_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_user_signer_safe_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
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

# **remove_user_signer_web3_wallet**
> BaseResponse remove_user_signer_web3_wallet(user_id, wallet_address)

Remove user web3 wallet signer

Removes a web3 wallet signer from a user.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 
    wallet_address = 'wallet_address_example' # str | An Ethereum address.

    try:
        # Remove user web3 wallet signer
        api_response = api_instance.remove_user_signer_web3_wallet(user_id, wallet_address)
        print("The response of AdminApi->remove_user_signer_web3_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_user_signer_web3_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
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

# **set_user_signer_cloud_wallet**
> BaseResponse set_user_signer_cloud_wallet(user_id, wallet_address)

Add or update user cloud wallet signer

Adds or updates a user's cloud wallet signer.

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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 
    wallet_address = 'wallet_address_example' # str | An Ethereum address.

    try:
        # Add or update user cloud wallet signer
        api_response = api_instance.set_user_signer_cloud_wallet(user_id, wallet_address)
        print("The response of AdminApi->set_user_signer_cloud_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_user_signer_cloud_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
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

# **set_user_signer_safe_account**
> BaseResponse set_user_signer_safe_account(user_id, wallet_address, signer_label)

Add or update user safe account signer

Adds or updates a user's safe account signer.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.signer_label import SignerLabel
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 
    wallet_address = 'wallet_address_example' # str | An Ethereum address.
    signer_label = multibaas_sdk.SignerLabel() # SignerLabel | 

    try:
        # Add or update user safe account signer
        api_response = api_instance.set_user_signer_safe_account(user_id, wallet_address, signer_label)
        print("The response of AdminApi->set_user_signer_safe_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_user_signer_safe_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **wallet_address** | **str**| An Ethereum address. | 
 **signer_label** | [**SignerLabel**](SignerLabel.md)|  | 

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

# **set_user_signer_web3_wallet**
> BaseResponse set_user_signer_web3_wallet(user_id, wallet_address, signer_label)

Add or update user web3 wallet signer

Adds or updates a user's web3 wallet signer.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.signer_label import SignerLabel
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    user_id = 56 # int | 
    wallet_address = 'wallet_address_example' # str | An Ethereum address.
    signer_label = multibaas_sdk.SignerLabel() # SignerLabel | 

    try:
        # Add or update user web3 wallet signer
        api_response = api_instance.set_user_signer_web3_wallet(user_id, wallet_address, signer_label)
        print("The response of AdminApi->set_user_signer_web3_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_user_signer_web3_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **wallet_address** | **str**| An Ethereum address. | 
 **signer_label** | [**SignerLabel**](SignerLabel.md)|  | 

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

# **update_api_key**
> BaseResponse update_api_key(api_key_id, base_api_key)

Update API key

Updates an API key.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_api_key import BaseAPIKey
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
    api_instance = multibaas_sdk.AdminApi(api_client)
    api_key_id = 56 # int | 
    base_api_key = multibaas_sdk.BaseAPIKey() # BaseAPIKey | 

    try:
        # Update API key
        api_response = api_instance.update_api_key(api_key_id, base_api_key)
        print("The response of AdminApi->update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**|  | 
 **base_api_key** | [**BaseAPIKey**](BaseAPIKey.md)|  | 

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

