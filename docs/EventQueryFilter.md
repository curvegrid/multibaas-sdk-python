# EventQueryFilter

A event query filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | The rule type, can be omitted if this is the last filter to be applied. | [optional] 
**field_type** | [**FieldType**](FieldType.md) |  | [optional] 
**input_index** | **int** | The field&#39;s index, can be used in place of &#x60;name&#x60;. | [optional] 
**operator** | **str** | The operator on the filter. | [optional] 
**value** | **str** | The value to be compared with. | [optional] 
**children** | [**List[EventQueryFilter]**](EventQueryFilter.md) | Other filters to be applied in succession with the rule specified. | [optional] 

## Example

```python
from multibaas_sdk.models.event_query_filter import EventQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventQueryFilter from a JSON string
event_query_filter_instance = EventQueryFilter.from_json(json)
# print the JSON string representation of the object
print(EventQueryFilter.to_json())

# convert the object into a dict
event_query_filter_dict = event_query_filter_instance.to_dict()
# create an instance of EventQueryFilter from a dict
event_query_filter_from_dict = EventQueryFilter.from_dict(event_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


