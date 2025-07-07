# EventQueryEvent

A query on a single event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | The name of an event. | 
**select** | [**List[EventQueryField]**](EventQueryField.md) | The query information about all the fields to select from an event. | 
**filter** | [**EventQueryFilter**](EventQueryFilter.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.event_query_event import EventQueryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EventQueryEvent from a JSON string
event_query_event_instance = EventQueryEvent.from_json(json)
# print the JSON string representation of the object
print(EventQueryEvent.to_json())

# convert the object into a dict
event_query_event_dict = event_query_event_instance.to_dict()
# create an instance of EventQueryEvent from a dict
event_query_event_from_dict = EventQueryEvent.from_dict(event_query_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


