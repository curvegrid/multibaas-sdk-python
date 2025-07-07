# GetEventCount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | **int** | The number of events. | 

## Example

```python
from multibaas_sdk.models.get_event_count200_response import GetEventCount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventCount200Response from a JSON string
get_event_count200_response_instance = GetEventCount200Response.from_json(json)
# print the JSON string representation of the object
print(GetEventCount200Response.to_json())

# convert the object into a dict
get_event_count200_response_dict = get_event_count200_response_instance.to_dict()
# create an instance of GetEventCount200Response from a dict
get_event_count200_response_from_dict = GetEventCount200Response.from_dict(get_event_count200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


