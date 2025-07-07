# ChainStatus

The status of the Chain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_number** | **int** |  | 
**version** | **str** | The client version for this chain node. | 
**chain_id** | **int** |  | 
**network_id** | **int** |  | 
**base_fee** | **str** | The current base fee (only available for chains that support EIP-1559). | [optional] 

## Example

```python
from multibaas_sdk.models.chain_status import ChainStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ChainStatus from a JSON string
chain_status_instance = ChainStatus.from_json(json)
# print the JSON string representation of the object
print(ChainStatus.to_json())

# convert the object into a dict
chain_status_dict = chain_status_instance.to_dict()
# create an instance of ChainStatus from a dict
chain_status_from_dict = ChainStatus.from_dict(chain_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


