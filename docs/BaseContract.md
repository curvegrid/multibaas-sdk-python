# BaseContract

A contract.

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

## Example

```python
from multibaas_sdk.models.base_contract import BaseContract

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContract from a JSON string
base_contract_instance = BaseContract.from_json(json)
# print the JSON string representation of the object
print(BaseContract.to_json())

# convert the object into a dict
base_contract_dict = base_contract_instance.to_dict()
# create an instance of BaseContract from a dict
base_contract_from_dict = BaseContract.from_dict(base_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


