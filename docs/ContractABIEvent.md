# ContractABIEvent

A contract event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**name** | **str** |  | 
**signature** | **str** |  | 
**anonymous** | **bool** |  | 
**inputs** | [**List[ContractABIEventArgument]**](ContractABIEventArgument.md) | List of contract event&#39;s input arguments. | 
**notes** | **str** | The developer documentation. | 
**description** | **str** | The user documentation. | 

## Example

```python
from multibaas_sdk.models.contract_abi_event import ContractABIEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ContractABIEvent from a JSON string
contract_abi_event_instance = ContractABIEvent.from_json(json)
# print the JSON string representation of the object
print(ContractABIEvent.to_json())

# convert the object into a dict
contract_abi_event_dict = contract_abi_event_instance.to_dict()
# create an instance of ContractABIEvent from a dict
contract_abi_event_from_dict = ContractABIEvent.from_dict(contract_abi_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


