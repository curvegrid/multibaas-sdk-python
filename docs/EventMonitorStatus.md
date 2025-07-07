# EventMonitorStatus

Status of an Event Monitor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **int** |  | [optional] 
**address_id** | **int** |  | [optional] 
**is_processing_past_logs** | **bool** |  | 
**ideal_block_range** | **int** |  | [optional] 
**latest_block_number** | **int** |  | 
**latest_block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**start_block_number** | **int** |  | 
**start_block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**updated_at** | **str** |  | 

## Example

```python
from multibaas_sdk.models.event_monitor_status import EventMonitorStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EventMonitorStatus from a JSON string
event_monitor_status_instance = EventMonitorStatus.from_json(json)
# print the JSON string representation of the object
print(EventMonitorStatus.to_json())

# convert the object into a dict
event_monitor_status_dict = event_monitor_status_instance.to_dict()
# create an instance of EventMonitorStatus from a dict
event_monitor_status_from_dict = EventMonitorStatus.from_dict(event_monitor_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


