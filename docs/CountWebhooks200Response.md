# CountWebhooks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | **int** | The webhook count. | 

## Example

```python
from multibaas_sdk.models.count_webhooks200_response import CountWebhooks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CountWebhooks200Response from a JSON string
count_webhooks200_response_instance = CountWebhooks200Response.from_json(json)
# print the JSON string representation of the object
print(CountWebhooks200Response.to_json())

# convert the object into a dict
count_webhooks200_response_dict = count_webhooks200_response_instance.to_dict()
# create an instance of CountWebhooks200Response from a dict
count_webhooks200_response_from_dict = CountWebhooks200Response.from_dict(count_webhooks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


