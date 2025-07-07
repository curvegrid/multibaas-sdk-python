# ExecuteArbitraryEventQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**EventQueryResults**](EventQueryResults.md) |  | 

## Example

```python
from multibaas_sdk.models.execute_arbitrary_event_query200_response import ExecuteArbitraryEventQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteArbitraryEventQuery200Response from a JSON string
execute_arbitrary_event_query200_response_instance = ExecuteArbitraryEventQuery200Response.from_json(json)
# print the JSON string representation of the object
print(ExecuteArbitraryEventQuery200Response.to_json())

# convert the object into a dict
execute_arbitrary_event_query200_response_dict = execute_arbitrary_event_query200_response_instance.to_dict()
# create an instance of ExecuteArbitraryEventQuery200Response from a dict
execute_arbitrary_event_query200_response_from_dict = ExecuteArbitraryEventQuery200Response.from_dict(execute_arbitrary_event_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


