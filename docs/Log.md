# Log

A contract log event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An ethereum address. | 
**topics** | **List[str]** | A list of topics provided by the contract. | 
**data** | **str** | A hex string. | 
**block_number** | **str** | A hex string. | 
**transaction_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**transaction_index** | **str** | A hex string. | 
**block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**log_index** | **str** | A hex string. | 
**removed** | **bool** | True if this log was reverted due to a chain reorganization. | 

## Example

```python
from multibaas_sdk.models.log import Log

# TODO update the JSON string below
json = "{}"
# create an instance of Log from a JSON string
log_instance = Log.from_json(json)
# print the JSON string representation of the object
print(Log.to_json())

# convert the object into a dict
log_dict = log_instance.to_dict()
# create an instance of Log from a dict
log_from_dict = Log.from_dict(log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


