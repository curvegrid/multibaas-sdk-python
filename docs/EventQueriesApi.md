# multibaas_sdk.EventQueriesApi

All URIs are relative to *https://your_deployment.multibaas.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_event_query_records**](EventQueriesApi.md#count_event_query_records) | **GET** /queries/{event_query}/count | Count event query records
[**delete_event_query**](EventQueriesApi.md#delete_event_query) | **DELETE** /queries/{event_query} | Delete event query
[**execute_arbitrary_event_query**](EventQueriesApi.md#execute_arbitrary_event_query) | **POST** /queries | Execute arbitrary event query
[**execute_event_query**](EventQueriesApi.md#execute_event_query) | **GET** /queries/{event_query}/results | Execute event query
[**get_event_query**](EventQueriesApi.md#get_event_query) | **GET** /queries/{event_query} | Get event query
[**list_event_queries**](EventQueriesApi.md#list_event_queries) | **GET** /queries | List event queries
[**set_event_query**](EventQueriesApi.md#set_event_query) | **PUT** /queries/{event_query} | Create or update event query


# **count_event_query_records**
> CountEventQueryRecords200Response count_event_query_records(event_query)

Count event query records

Returns the record count of the given saved event query.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.count_event_query_records200_response import CountEventQueryRecords200Response
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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)
    event_query = 'event_query_example' # str | An event query label.

    try:
        # Count event query records
        api_response = api_instance.count_event_query_records(event_query)
        print("The response of EventQueriesApi->count_event_query_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->count_event_query_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_query** | **str**| An event query label. | 

### Return type

[**CountEventQueryRecords200Response**](CountEventQueryRecords200Response.md)

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

# **delete_event_query**
> BaseResponse delete_event_query(event_query)

Delete event query

Deletes the given saved event query.

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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)
    event_query = 'event_query_example' # str | An event query label.

    try:
        # Delete event query
        api_response = api_instance.delete_event_query(event_query)
        print("The response of EventQueriesApi->delete_event_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->delete_event_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_query** | **str**| An event query label. | 

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

# **execute_arbitrary_event_query**
> ExecuteArbitraryEventQuery200Response execute_arbitrary_event_query(event_query, offset=offset, limit=limit)

Execute arbitrary event query

Executes an arbitrary event query.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.event_query import EventQuery
from multibaas_sdk.models.execute_arbitrary_event_query200_response import ExecuteArbitraryEventQuery200Response
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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)
    event_query = multibaas_sdk.EventQuery() # EventQuery | 
    offset = 56 # int |  (optional)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Execute arbitrary event query
        api_response = api_instance.execute_arbitrary_event_query(event_query, offset=offset, limit=limit)
        print("The response of EventQueriesApi->execute_arbitrary_event_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->execute_arbitrary_event_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_query** | [**EventQuery**](EventQuery.md)|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**ExecuteArbitraryEventQuery200Response**](ExecuteArbitraryEventQuery200Response.md)

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

# **execute_event_query**
> ExecuteArbitraryEventQuery200Response execute_event_query(event_query, offset=offset, limit=limit)

Execute event query

Executes the given saved event query.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.execute_arbitrary_event_query200_response import ExecuteArbitraryEventQuery200Response
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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)
    event_query = 'event_query_example' # str | An event query label.
    offset = 56 # int |  (optional)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Execute event query
        api_response = api_instance.execute_event_query(event_query, offset=offset, limit=limit)
        print("The response of EventQueriesApi->execute_event_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->execute_event_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_query** | **str**| An event query label. | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**ExecuteArbitraryEventQuery200Response**](ExecuteArbitraryEventQuery200Response.md)

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

# **get_event_query**
> GetEventQuery200Response get_event_query(event_query)

Get event query

Returns the given saved event query.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.get_event_query200_response import GetEventQuery200Response
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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)
    event_query = 'event_query_example' # str | An event query label.

    try:
        # Get event query
        api_response = api_instance.get_event_query(event_query)
        print("The response of EventQueriesApi->get_event_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->get_event_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_query** | **str**| An event query label. | 

### Return type

[**GetEventQuery200Response**](GetEventQuery200Response.md)

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

# **list_event_queries**
> ListEventQueries200Response list_event_queries()

List event queries

Returns a list of saved event queries.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.list_event_queries200_response import ListEventQueries200Response
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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)

    try:
        # List event queries
        api_response = api_instance.list_event_queries()
        print("The response of EventQueriesApi->list_event_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->list_event_queries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListEventQueries200Response**](ListEventQueries200Response.md)

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

# **set_event_query**
> BaseResponse set_event_query(event_query, event_query2)

Create or update event query

Creates or updates the given saved event query.

### Example

* Api Key Authentication (cookie):
* Bearer (JWT) Authentication (bearer):

```python
import multibaas_sdk
from multibaas_sdk.models.base_response import BaseResponse
from multibaas_sdk.models.event_query import EventQuery
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
    api_instance = multibaas_sdk.EventQueriesApi(api_client)
    event_query = 'event_query_example' # str | An event query label.
    event_query2 = multibaas_sdk.EventQuery() # EventQuery | 

    try:
        # Create or update event query
        api_response = api_instance.set_event_query(event_query, event_query2)
        print("The response of EventQueriesApi->set_event_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventQueriesApi->set_event_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_query** | **str**| An event query label. | 
 **event_query2** | [**EventQuery**](EventQuery.md)|  | 

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

