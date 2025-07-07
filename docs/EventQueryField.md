# EventQueryField

A single event field's query information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FieldType**](FieldType.md) |  | 
**name** | **str** | The field name. Either &#x60;name&#x60; or &#x60;inputIndex&#x60; is required if &#x60;fieldType &#x3D;&#x3D; \&quot;input\&quot;&#x60;. | [optional] 
**input_index** | **int** | The field&#39;s index, can be used in place of &#x60;name&#x60;. | [optional] 
**alias** | **str** | The name that will be used to return the field. | [optional] 
**aggregator** | **str** | The type of aggregation to perform on the field. | [optional] 

## Example

```python
from multibaas_sdk.models.event_query_field import EventQueryField

# TODO update the JSON string below
json = "{}"
# create an instance of EventQueryField from a JSON string
event_query_field_instance = EventQueryField.from_json(json)
# print the JSON string representation of the object
print(EventQueryField.to_json())

# convert the object into a dict
event_query_field_dict = event_query_field_instance.to_dict()
# create an instance of EventQueryField from a dict
event_query_field_from_dict = EventQueryField.from_dict(event_query_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


