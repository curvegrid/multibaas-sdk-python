# ContractABI

The contract ABI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constructor** | [**ContractABIMethod**](ContractABIMethod.md) |  | 
**methods** | [**Dict[str, ContractABIMethod]**](ContractABIMethod.md) |  | 
**events** | [**Dict[str, ContractABIEvent]**](ContractABIEvent.md) |  | 
**errors** | [**Dict[str, ContractABIError]**](ContractABIError.md) |  | [optional] 
**fallback** | [**ContractABIMethod**](ContractABIMethod.md) |  | 
**receive** | [**ContractABIMethod**](ContractABIMethod.md) |  | 

## Example

```python
from multibaas_sdk.models.contract_abi import ContractABI

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABI from a JSON string
contract_abi_instance = ContractABI.from_json(json)
# print the JSON string representation of the object
print(ContractABI.to_json())

# convert the object into a dict
contract_abi_dict = contract_abi_instance.to_dict()
# create an instance of ContractABI from a dict
contract_abi_from_dict = ContractABI.from_dict(contract_abi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


