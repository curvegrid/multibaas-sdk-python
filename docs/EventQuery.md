# EventQuery

An event query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventQueryEvent]**](EventQueryEvent.md) |  | 
**group_by** | **str** | The results will be grouped according to this field. An aggregator for non Group By fields must be specified if groupBy is specified. | [optional] 
**order_by** | **str** | The results will be ordered according to this field. | [optional] 
**order** | **str** | Specify ascending or descending order, the default is \&quot;ASC\&quot;. | [optional] 

## Example

```python
from multibaas_sdk.models.event_query import EventQuery

# TODO update the JSON string below
json = "{}"
# create an instance of EventQuery from a JSON string
event_query_instance = EventQuery.from_json(json)
# print the JSON string representation of the object
print(EventQuery.to_json())

# convert the object into a dict
event_query_dict = event_query_instance.to_dict()
# create an instance of EventQuery from a dict
event_query_from_dict = EventQuery.from_dict(event_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


