# ContractParameter

Type conversion options for an input or an output of a function or an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_conversion** | [**ContractABITypeConversion**](ContractABITypeConversion.md) |  | 

## Example

```python
from multibaas_sdk.models.contract_parameter import ContractParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ContractParameter from a JSON string
contract_parameter_instance = ContractParameter.from_json(json)
# print the JSON string representation of the object
print(ContractParameter.to_json())

# convert the object into a dict
contract_parameter_dict = contract_parameter_instance.to_dict()
# create an instance of ContractParameter from a dict
contract_parameter_from_dict = ContractParameter.from_dict(contract_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


