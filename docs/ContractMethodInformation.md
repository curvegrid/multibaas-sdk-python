# ContractMethodInformation

The contract method's information returned within the event or transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the method. | 
**signature** | **str** | The method signature. | 
**inputs** | [**List[MethodArg]**](MethodArg.md) |  | 

## Example

```python
from multibaas_sdk.models.contract_method_information import ContractMethodInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ContractMethodInformation from a JSON string
contract_method_information_instance = ContractMethodInformation.from_json(json)
# print the JSON string representation of the object
print(ContractMethodInformation.to_json())

# convert the object into a dict
contract_method_information_dict = contract_method_information_instance.to_dict()
# create an instance of ContractMethodInformation from a dict
contract_method_information_from_dict = ContractMethodInformation.from_dict(contract_method_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


