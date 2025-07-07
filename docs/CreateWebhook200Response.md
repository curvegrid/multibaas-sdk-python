# CreateWebhook200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**WebhookEndpoint**](WebhookEndpoint.md) |  | 

## Example

```python
from multibaas_sdk.models.create_webhook200_response import CreateWebhook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhook200Response from a JSON string
create_webhook200_response_instance = CreateWebhook200Response.from_json(json)
# print the JSON string representation of the object
print(CreateWebhook200Response.to_json())

# convert the object into a dict
create_webhook200_response_dict = create_webhook200_response_instance.to_dict()
# create an instance of CreateWebhook200Response from a dict
create_webhook200_response_from_dict = CreateWebhook200Response.from_dict(create_webhook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


