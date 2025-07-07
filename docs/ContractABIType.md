# ContractABIType

A contract function or event argument type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**size** | **int** |  | [optional] 
**tuple_elems** | [**List[ContractABIType]**](ContractABIType.md) |  | [optional] 
**tuple_raw_names** | **List[str]** |  | [optional] 
**elem** | [**ContractABIType**](ContractABIType.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.contract_abi_type import ContractABIType

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIType from a JSON string
contract_abi_type_instance = ContractABIType.from_json(json)
# print the JSON string representation of the object
print(ContractABIType.to_json())

# convert the object into a dict
contract_abi_type_dict = contract_abi_type_instance.to_dict()
# create an instance of ContractABIType from a dict
contract_abi_type_from_dict = ContractABIType.from_dict(contract_abi_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


