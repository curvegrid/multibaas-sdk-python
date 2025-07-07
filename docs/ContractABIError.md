# ContractABIError

A contract error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**name** | **str** |  | 
**signature** | **str** |  | 
**inputs** | [**List[ContractABIErrorArgument]**](ContractABIErrorArgument.md) | List of contract event&#39;s input arguments. | 
**notes** | **str** | The developer documentation. | [optional] 
**description** | **str** | The user documentation. | [optional] 

## Example

```python
from multibaas_sdk.models.contract_abi_error import ContractABIError

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIError from a JSON string
contract_abi_error_instance = ContractABIError.from_json(json)
# print the JSON string representation of the object
print(ContractABIError.to_json())

# convert the object into a dict
contract_abi_error_dict = contract_abi_error_instance.to_dict()
# create an instance of ContractABIError from a dict
contract_abi_error_from_dict = ContractABIError.from_dict(contract_abi_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


