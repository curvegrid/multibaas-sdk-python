# SavedEventQuery

A saved event query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**label** | **str** | An event query label. | 
**query** | [**EventQuery**](EventQuery.md) |  | 
**is_system** | **bool** | Specifies if this a system-generated query which is not modifiable by the user. | 

## Example

```python
from multibaas_sdk.models.saved_event_query import SavedEventQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SavedEventQuery from a JSON string
saved_event_query_instance = SavedEventQuery.from_json(json)
# print the JSON string representation of the object
print(SavedEventQuery.to_json())

# convert the object into a dict
saved_event_query_dict = saved_event_query_instance.to_dict()
# create an instance of SavedEventQuery from a dict
saved_event_query_from_dict = SavedEventQuery.from_dict(saved_event_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


