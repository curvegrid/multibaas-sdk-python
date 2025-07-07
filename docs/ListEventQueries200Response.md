# ListEventQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**List[SavedEventQuery]**](SavedEventQuery.md) |  | 

## Example

```python
from multibaas_sdk.models.list_event_queries200_response import ListEventQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListEventQueries200Response from a JSON string
list_event_queries200_response_instance = ListEventQueries200Response.from_json(json)
# print the JSON string representation of the object
print(ListEventQueries200Response.to_json())

# convert the object into a dict
list_event_queries200_response_dict = list_event_queries200_response_instance.to_dict()
# create an instance of ListEventQueries200Response from a dict
list_event_queries200_response_from_dict = ListEventQueries200Response.from_dict(list_event_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


