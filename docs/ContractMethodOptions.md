# ContractMethodOptions

Type conversion options for a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | The function signature. | [optional] 
**inputs** | [**List[ContractParameter]**](ContractParameter.md) | List of function input parameters. | 
**outputs** | [**List[ContractParameter]**](ContractParameter.md) | List of function output parameters. | [optional] 

## Example

```python
from multibaas_sdk.models.contract_method_options import ContractMethodOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ContractMethodOptions from a JSON string
contract_method_options_instance = ContractMethodOptions.from_json(json)
# print the JSON string representation of the object
print(ContractMethodOptions.to_json())

# convert the object into a dict
contract_method_options_dict = contract_method_options_instance.to_dict()
# create an instance of ContractMethodOptions from a dict
contract_method_options_from_dict = ContractMethodOptions.from_dict(contract_method_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


