# Contract

A returned contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**contract_name** | **str** | The name of the contract. | 
**version** | **str** | The contract version. | 
**bin** | **str** | The smart-contract bytecode. | [optional] 
**raw_abi** | **str** | The contract raw ABI JSON string. | 
**user_doc** | **str** | The user documentation JSON string. | [optional] 
**developer_doc** | **str** | The developer documentation JSON string. | [optional] 
**metadata** | **str** | The contract metadata JSON string. | [optional] 
**is_favorite** | **bool** |  | [optional] 
**abi** | [**ContractABI**](ContractABI.md) |  | 
**instances** | [**List[ContractInstance]**](ContractInstance.md) | List of the contract instances. | [optional] 

## Example

```python
from multibaas_sdk.models.contract import Contract

# TODO update the JSON string below
json = "{}"
# create an instance of Contract from a JSON string
contract_instance = Contract.from_json(json)
# print the JSON string representation of the object
print(Contract.to_json())

# convert the object into a dict
contract_dict = contract_instance.to_dict()
# create an instance of Contract from a dict
contract_from_dict = Contract.from_dict(contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


