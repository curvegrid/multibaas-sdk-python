# EventQueryResults

Results of an executed event query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[Dict[str, object]]** |  | 

## Example

```python
from multibaas_sdk.models.event_query_results import EventQueryResults

# TODO update the JSON string below
json = "{}"
# create an instance of EventQueryResults from a JSON string
event_query_results_instance = EventQueryResults.from_json(json)
# print the JSON string representation of the object
print(EventQueryResults.to_json())

# convert the object into a dict
event_query_results_dict = event_query_results_instance.to_dict()
# create an instance of EventQueryResults from a dict
event_query_results_from_dict = EventQueryResults.from_dict(event_query_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


