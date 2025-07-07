# ContractABIMethodArgument

A contract function argument.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**ContractABIType**](ContractABIType.md) |  | 
**type_name** | **str** |  | 
**type_conversion** | [**ContractABITypeConversion**](ContractABITypeConversion.md) |  | 
**notes** | **str** |  | 

## Example

```python
from multibaas_sdk.models.contract_abi_method_argument import ContractABIMethodArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIMethodArgument from a JSON string
contract_abi_method_argument_instance = ContractABIMethodArgument.from_json(json)
# print the JSON string representation of the object
print(ContractABIMethodArgument.to_json())

# convert the object into a dict
contract_abi_method_argument_dict = contract_abi_method_argument_instance.to_dict()
# create an instance of ContractABIMethodArgument from a dict
contract_abi_method_argument_from_dict = ContractABIMethodArgument.from_dict(contract_abi_method_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


