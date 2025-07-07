# ContractEventOptions

Type conversion options for an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** |  | [optional] 
**inputs** | [**List[ContractParameter]**](ContractParameter.md) |  | 

## Example

```python
from multibaas_sdk.models.contract_event_options import ContractEventOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ContractEventOptions from a JSON string
contract_event_options_instance = ContractEventOptions.from_json(json)
# print the JSON string representation of the object
print(ContractEventOptions.to_json())

# convert the object into a dict
contract_event_options_dict = contract_event_options_instance.to_dict()
# create an instance of ContractEventOptions from a dict
contract_event_options_from_dict = ContractEventOptions.from_dict(contract_event_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


