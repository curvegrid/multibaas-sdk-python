# EIP712Types

A mapping of type names to arrays of fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eip712_domain** | [**List[EIP712TypeEntry]**](EIP712TypeEntry.md) |  | 

## Example

```python
from multibaas_sdk.models.eip712_types import EIP712Types

# TODO update the JSON string below
json = "{}"
# create an instance of EIP712Types from a JSON string
eip712_types_instance = EIP712Types.from_json(json)
# print the JSON string representation of the object
print(EIP712Types.to_json())

# convert the object into a dict
eip712_types_dict = eip712_types_instance.to_dict()
# create an instance of EIP712Types from a dict
eip712_types_from_dict = EIP712Types.from_dict(eip712_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


