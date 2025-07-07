# EIP712TypeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from multibaas_sdk.models.eip712_type_entry import EIP712TypeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EIP712TypeEntry from a JSON string
eip712_type_entry_instance = EIP712TypeEntry.from_json(json)
# print the JSON string representation of the object
print(EIP712TypeEntry.to_json())

# convert the object into a dict
eip712_type_entry_dict = eip712_type_entry_instance.to_dict()
# create an instance of EIP712TypeEntry from a dict
eip712_type_entry_from_dict = EIP712TypeEntry.from_dict(eip712_type_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


