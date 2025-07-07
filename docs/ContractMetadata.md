# ContractMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**name** | **str** | The name of the contract. | 
**version** | **str** | The contract version. | 

## Example

```python
from multibaas_sdk.models.contract_metadata import ContractMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ContractMetadata from a JSON string
contract_metadata_instance = ContractMetadata.from_json(json)
# print the JSON string representation of the object
print(ContractMetadata.to_json())

# convert the object into a dict
contract_metadata_dict = contract_metadata_instance.to_dict()
# create an instance of ContractMetadata from a dict
contract_metadata_from_dict = ContractMetadata.from_dict(contract_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


