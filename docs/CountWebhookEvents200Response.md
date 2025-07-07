# CountWebhookEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | **int** | The number of webhook events. | 

## Example

```python
from multibaas_sdk.models.count_webhook_events200_response import CountWebhookEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CountWebhookEvents200Response from a JSON string
count_webhook_events200_response_instance = CountWebhookEvents200Response.from_json(json)
# print the JSON string representation of the object
print(CountWebhookEvents200Response.to_json())

# convert the object into a dict
count_webhook_events200_response_dict = count_webhook_events200_response_instance.to_dict()
# create an instance of CountWebhookEvents200Response from a dict
count_webhook_events200_response_from_dict = CountWebhookEvents200Response.from_dict(count_webhook_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


