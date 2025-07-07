# ContractABITypeConversion

Holds JSON-compatible type conversion information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**decimals_absolute** | **int** |  | 
**decimals_function** | **str** |  | 

## Example

```python
from multibaas_sdk.models.contract_abi_type_conversion import ContractABITypeConversion

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABITypeConversion from a JSON string
contract_abi_type_conversion_instance = ContractABITypeConversion.from_json(json)
# print the JSON string representation of the object
print(ContractABITypeConversion.to_json())

# convert the object into a dict
contract_abi_type_conversion_dict = contract_abi_type_conversion_instance.to_dict()
# create an instance of ContractABITypeConversion from a dict
contract_abi_type_conversion_from_dict = ContractABITypeConversion.from_dict(contract_abi_type_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


