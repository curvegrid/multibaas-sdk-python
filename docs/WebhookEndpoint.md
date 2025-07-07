# WebhookEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send the webhook to. | 
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**subscriptions** | [**List[WebhookEventsType]**](WebhookEventsType.md) | The events to subscribe to. | 
**id** | **int** |  | 
**next_attempt** | **datetime** | The time the next attempt will be made. | [optional] 
**last_attempt** | **datetime** | The time the last attempt was made. | [optional] 
**failed_calls** | **int** | The number of failed webhook endpoint calls since the last successful call. | 
**last_error** | **str** | The last error received from the webhook endpoint. | [optional] 
**created_at** | **datetime** | The time the webhook was created. | 
**updated_at** | **datetime** | The time the webhook was last updated. | 
**secret** | **str** | The secret key used to sign the webhook. | 

## Example

```python
from multibaas_sdk.models.webhook_endpoint import WebhookEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEndpoint from a JSON string
webhook_endpoint_instance = WebhookEndpoint.from_json(json)
# print the JSON string representation of the object
print(WebhookEndpoint.to_json())

# convert the object into a dict
webhook_endpoint_dict = webhook_endpoint_instance.to_dict()
# create an instance of WebhookEndpoint from a dict
webhook_endpoint_from_dict = WebhookEndpoint.from_dict(webhook_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


