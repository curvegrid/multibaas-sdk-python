# EventField

Holds a field in the event's data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The input name. | 
**value** | **object** | The input value. | 
**hashed** | **bool** | Has the value been hashed into a keccak256 string? | 
**type** | **str** | The type of the argument. | 

## Example

```python
from multibaas_sdk.models.event_field import EventField

# TODO update the JSON string below
json = "{}"
# create an instance of EventField from a JSON string
event_field_instance = EventField.from_json(json)
# print the JSON string representation of the object
print(EventField.to_json())

# convert the object into a dict
event_field_dict = event_field_instance.to_dict()
# create an instance of EventField from a dict
event_field_from_dict = EventField.from_dict(event_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


