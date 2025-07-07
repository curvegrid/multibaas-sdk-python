# ContractABIErrorArgument

A contract error argument.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**ContractABIType**](ContractABIType.md) |  | 
**type_name** | **str** |  | 
**indexed** | **bool** |  | 
**notes** | **str** | The developer documentation. | 

## Example

```python
from multibaas_sdk.models.contract_abi_error_argument import ContractABIErrorArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIErrorArgument from a JSON string
contract_abi_error_argument_instance = ContractABIErrorArgument.from_json(json)
# print the JSON string representation of the object
print(ContractABIErrorArgument.to_json())

# convert the object into a dict
contract_abi_error_argument_dict = contract_abi_error_argument_instance.to_dict()
# create an instance of ContractABIErrorArgument from a dict
contract_abi_error_argument_from_dict = ContractABIErrorArgument.from_dict(contract_abi_error_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


