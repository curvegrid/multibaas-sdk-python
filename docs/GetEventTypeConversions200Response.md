# GetEventTypeConversions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**EventTypeConversionOptions**](EventTypeConversionOptions.md) |  | 

## Example

```python
from multibaas_sdk.models.get_event_type_conversions200_response import GetEventTypeConversions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventTypeConversions200Response from a JSON string
get_event_type_conversions200_response_instance = GetEventTypeConversions200Response.from_json(json)
# print the JSON string representation of the object
print(GetEventTypeConversions200Response.to_json())

# convert the object into a dict
get_event_type_conversions200_response_dict = get_event_type_conversions200_response_instance.to_dict()
# create an instance of GetEventTypeConversions200Response from a dict
get_event_type_conversions200_response_from_dict = GetEventTypeConversions200Response.from_dict(get_event_type_conversions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


