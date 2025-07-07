# EventInformation

The event information returned as part of an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the event. | 
**signature** | **str** | The event signature. | 
**inputs** | [**List[EventField]**](EventField.md) | The list of input arguments for the event. | 
**raw_fields** | **str** | The raw output from an event. Omitted when returned as part of a transaction receipt. | [optional] 
**contract** | [**ContractInformation**](ContractInformation.md) |  | 
**index_in_log** | **int** | The event&#39;s index in the log. | 

## Example

```python
from multibaas_sdk.models.event_information import EventInformation

# TODO update the JSON string below
json = "{}"
# create an instance of EventInformation from a JSON string
event_information_instance = EventInformation.from_json(json)
# print the JSON string representation of the object
print(EventInformation.to_json())

# convert the object into a dict
event_information_dict = event_information_instance.to_dict()
# create an instance of EventInformation from a dict
event_information_from_dict = EventInformation.from_dict(event_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


