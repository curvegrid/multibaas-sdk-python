# ContractInformation

The contract information within the event or transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An ethereum address. | 
**address_alias** | **str** | An alias to easily identify and reference addresses. | 
**name** | **str** | The name of the contract. | 
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 

## Example

```python
from multibaas_sdk.models.contract_information import ContractInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ContractInformation from a JSON string
contract_information_instance = ContractInformation.from_json(json)
# print the JSON string representation of the object
print(ContractInformation.to_json())

# convert the object into a dict
contract_information_dict = contract_information_instance.to_dict()
# create an instance of ContractInformation from a dict
contract_information_from_dict = ContractInformation.from_dict(contract_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


