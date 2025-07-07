# CountEventQueryRecords200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | **int** | The record count. | 

## Example

```python
from multibaas_sdk.models.count_event_query_records200_response import CountEventQueryRecords200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CountEventQueryRecords200Response from a JSON string
count_event_query_records200_response_instance = CountEventQueryRecords200Response.from_json(json)
# print the JSON string representation of the object
print(CountEventQueryRecords200Response.to_json())

# convert the object into a dict
count_event_query_records200_response_dict = count_event_query_records200_response_instance.to_dict()
# create an instance of CountEventQueryRecords200Response from a dict
count_event_query_records200_response_from_dict = CountEventQueryRecords200Response.from_dict(count_event_query_records200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


