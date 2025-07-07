# GetEventQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**EventQuery**](EventQuery.md) |  | 

## Example

```python
from multibaas_sdk.models.get_event_query200_response import GetEventQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventQuery200Response from a JSON string
get_event_query200_response_instance = GetEventQuery200Response.from_json(json)
# print the JSON string representation of the object
print(GetEventQuery200Response.to_json())

# convert the object into a dict
get_event_query200_response_dict = get_event_query200_response_instance.to_dict()
# create an instance of GetEventQuery200Response from a dict
get_event_query200_response_from_dict = GetEventQuery200Response.from_dict(get_event_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


