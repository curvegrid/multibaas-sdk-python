# EventTypeConversionOptions

Type conversion options for each of the inputs of an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[TypeConversionOptions]**](TypeConversionOptions.md) | List of event&#39;s input parameters. | 

## Example

```python
from multibaas_sdk.models.event_type_conversion_options import EventTypeConversionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeConversionOptions from a JSON string
event_type_conversion_options_instance = EventTypeConversionOptions.from_json(json)
# print the JSON string representation of the object
print(EventTypeConversionOptions.to_json())

# convert the object into a dict
event_type_conversion_options_dict = event_type_conversion_options_instance.to_dict()
# create an instance of EventTypeConversionOptions from a dict
event_type_conversion_options_from_dict = EventTypeConversionOptions.from_dict(event_type_conversion_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


