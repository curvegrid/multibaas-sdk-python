# ContractOverview

A contract overview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**contract_name** | **str** | The name of the contract. | 
**version** | **str** | The contract version. | 
**is_favorite** | **bool** |  | [optional] 
**deployable** | **bool** |  | 
**instances** | [**List[ContractInstance]**](ContractInstance.md) | List of contract instances. | 

## Example

```python
from multibaas_sdk.models.contract_overview import ContractOverview

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOverview from a JSON string
contract_overview_instance = ContractOverview.from_json(json)
# print the JSON string representation of the object
print(ContractOverview.to_json())

# convert the object into a dict
contract_overview_dict = contract_overview_instance.to_dict()
# create an instance of ContractOverview from a dict
contract_overview_from_dict = ContractOverview.from_dict(contract_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


