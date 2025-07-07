# ContractABIMethod

A contract function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A hex string. | 
**name** | **str** | Name of the function. | 
**signature** | **str** | The function signature. | 
**const** | **bool** |  | 
**payable** | **bool** |  | 
**inputs** | [**List[ContractABIMethodArgument]**](ContractABIMethodArgument.md) | List of function arguments. | 
**outputs** | [**List[ContractABIMethodArgument]**](ContractABIMethodArgument.md) | List of function outputs. | 
**author** | **str** |  | 
**notes** | **str** |  | 
**description** | **str** | The function description. | 

## Example

```python
from multibaas_sdk.models.contract_abi_method import ContractABIMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIMethod from a JSON string
contract_abi_method_instance = ContractABIMethod.from_json(json)
# print the JSON string representation of the object
print(ContractABIMethod.to_json())

# convert the object into a dict
contract_abi_method_dict = contract_abi_method_instance.to_dict()
# create an instance of ContractABIMethod from a dict
contract_abi_method_from_dict = ContractABIMethod.from_dict(contract_abi_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


