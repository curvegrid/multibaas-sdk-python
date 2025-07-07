# Event

An event returned by the API call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triggered_at** | **datetime** | The time at which the event was triggered. | 
**event** | [**EventInformation**](EventInformation.md) |  | 
**transaction** | [**TransactionInformation**](TransactionInformation.md) |  | 

## Example

```python
from multibaas_sdk.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


