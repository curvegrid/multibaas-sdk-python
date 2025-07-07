# ContractLookup

The contract lookup item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An ethereum address. | 
**name** | **str** | The name of the contract. | [optional] 
**abi** | **str** | The contract ABI JSON string. | 
**bytecode** | **str** | The smart-contract bytecode. | [optional] 
**source** | **str** | The contract&#39;s source code. | [optional] 
**userdoc** | **str** | The user documentation JSON string. | [optional] 
**devdoc** | **str** | The developer documentation JSON string. | [optional] 
**verified** | **bool** | Indicates whether the contract has been verified. | 
**verified_source** | **str** | The name of the service that provided the contract verification. | [optional] 
**verified_link** | **str** | The URL to the contract&#39;s verification details on the verification service. | [optional] 
**proxy** | **bool** | Indicates whether the contract is a proxy contract. | 

## Example

```python
from multibaas_sdk.models.contract_lookup import ContractLookup

# TODO update the JSON string below
json = "{}"
# create an instance of ContractLookup from a JSON string
contract_lookup_instance = ContractLookup.from_json(json)
# print the JSON string representation of the object
print(ContractLookup.to_json())

# convert the object into a dict
contract_lookup_dict = contract_lookup_instance.to_dict()
# create an instance of ContractLookup from a dict
contract_lookup_from_dict = ContractLookup.from_dict(contract_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


