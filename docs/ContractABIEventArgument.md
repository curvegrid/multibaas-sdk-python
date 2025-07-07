# ContractABIEventArgument

A contract event argument.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**ContractABIType**](ContractABIType.md) |  | 
**type_name** | **str** |  | 
**indexed** | **bool** |  | 
**type_conversion** | [**ContractABITypeConversion**](ContractABITypeConversion.md) |  | 
**notes** | **str** | The developer documentation. | 

## Example

```python
from multibaas_sdk.models.contract_abi_event_argument import ContractABIEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIEventArgument from a JSON string
contract_abi_event_argument_instance = ContractABIEventArgument.from_json(json)
# print the JSON string representation of the object
print(ContractABIEventArgument.to_json())

# convert the object into a dict
contract_abi_event_argument_dict = contract_abi_event_argument_instance.to_dict()
# create an instance of ContractABIEventArgument from a dict
contract_abi_event_argument_from_dict = ContractABIEventArgument.from_dict(contract_abi_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


