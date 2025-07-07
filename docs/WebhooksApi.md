# multibaas_sdk.WebhooksApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_webhook_events**](WebhooksApi.md#count_webhook_events) | **GET** /webhooks/{webhookID}/events/count | Count webhook events
[**count_webhooks**](WebhooksApi.md#count_webhooks) | **GET** /webhooks/count | Count webhooks
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhookID} | Delete webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhookID} | Get webhook
[**list_webhook_events**](WebhooksApi.md#list_webhook_events) | **GET** /webhooks/{webhookID}/events | List webhook events
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /webhooks | List webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhookID} | Update webhook


# **count_webhook_events**
> CountWebhookEvents200Response count_webhook_events(webhook_id)

Count webhook events

Count the events for the given webhook endpoint.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.count_webhook_events200_response import CountWebhookEvents200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    webhook_id = 56 # int | 

    try:
        # Count webhook events
        api_response = api_instance.count_webhook_events(webhook_id)
        print("The response of WebhooksApi->count_webhook_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->count_webhook_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**|  | 

### Return type

[**CountWebhookEvents200Response**](CountWebhookEvents200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_webhooks**
> CountWebhooks200Response count_webhooks()

Count webhooks

Count all webhook endpoints.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.count_webhooks200_response import CountWebhooks200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)

    try:
        # Count webhooks
        api_response = api_instance.count_webhooks()
        print("The response of WebhooksApi->count_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->count_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CountWebhooks200Response**](CountWebhooks200Response.md)

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

# **create_webhook**
> CreateWebhook200Response create_webhook(base_webhook_endpoint)

Create webhook

Create a webhook.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_webhook_endpoint import BaseWebhookEndpoint
from multibaas_sdk.models.create_webhook200_response import CreateWebhook200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    base_webhook_endpoint = multibaas_sdk.BaseWebhookEndpoint() # BaseWebhookEndpoint | 

    try:
        # Create webhook
        api_response = api_instance.create_webhook(base_webhook_endpoint)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_webhook_endpoint** | [**BaseWebhookEndpoint**](BaseWebhookEndpoint.md)|  | 

### Return type

[**CreateWebhook200Response**](CreateWebhook200Response.md)

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

# **delete_webhook**
> BaseResponse delete_webhook(webhook_id)

Delete webhook

Delete a webhook endpoint.

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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    webhook_id = 56 # int | 

    try:
        # Delete webhook
        api_response = api_instance.delete_webhook(webhook_id)
        print("The response of WebhooksApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**|  | 

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

# **get_webhook**
> CreateWebhook200Response get_webhook(webhook_id)

Get webhook

Get a webhook endpoint.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.create_webhook200_response import CreateWebhook200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    webhook_id = 56 # int | 

    try:
        # Get webhook
        api_response = api_instance.get_webhook(webhook_id)
        print("The response of WebhooksApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**|  | 

### Return type

[**CreateWebhook200Response**](CreateWebhook200Response.md)

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

# **list_webhook_events**
> ListWebhookEvents200Response list_webhook_events(webhook_id, limit=limit, offset=offset)

List webhook events

List events for the given webhook endpoint.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_webhook_events200_response import ListWebhookEvents200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    webhook_id = 56 # int | 
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # List webhook events
        api_response = api_instance.list_webhook_events(webhook_id, limit=limit, offset=offset)
        print("The response of WebhooksApi->list_webhook_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhook_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**ListWebhookEvents200Response**](ListWebhookEvents200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> ListWebhooks200Response list_webhooks(limit=limit, offset=offset)

List webhooks

List all webhook endpoints.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_webhooks200_response import ListWebhooks200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # List webhooks
        api_response = api_instance.list_webhooks(limit=limit, offset=offset)
        print("The response of WebhooksApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**ListWebhooks200Response**](ListWebhooks200Response.md)

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

# **update_webhook**
> CreateWebhook200Response update_webhook(webhook_id, base_webhook_endpoint)

Update webhook

Update a webhook endpoint.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_webhook_endpoint import BaseWebhookEndpoint
from multibaas_sdk.models.create_webhook200_response import CreateWebhook200Response
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
    api_instance = multibaas_sdk.WebhooksApi(api_client)
    webhook_id = 56 # int | 
    base_webhook_endpoint = multibaas_sdk.BaseWebhookEndpoint() # BaseWebhookEndpoint | 

    try:
        # Update webhook
        api_response = api_instance.update_webhook(webhook_id, base_webhook_endpoint)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**|  | 
 **base_webhook_endpoint** | [**BaseWebhookEndpoint**](BaseWebhookEndpoint.md)|  | 

### Return type

[**CreateWebhook200Response**](CreateWebhook200Response.md)

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

