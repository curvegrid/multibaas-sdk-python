# BaseWebhookEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send the webhook to. | 
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**subscriptions** | [**List[WebhookEventsType]**](WebhookEventsType.md) | The events to subscribe to. | 

## Example

```python
from multibaas_sdk.models.base_webhook_endpoint import BaseWebhookEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of BaseWebhookEndpoint from a JSON string
base_webhook_endpoint_instance = BaseWebhookEndpoint.from_json(json)
# print the JSON string representation of the object
print(BaseWebhookEndpoint.to_json())

# convert the object into a dict
base_webhook_endpoint_dict = base_webhook_endpoint_instance.to_dict()
# create an instance of BaseWebhookEndpoint from a dict
base_webhook_endpoint_from_dict = BaseWebhookEndpoint.from_dict(base_webhook_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


