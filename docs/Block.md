# Block

A block in the Ethereum blockchain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**difficulty** | **str** |  | 
**gas_limit** | **int** |  | 
**number** | **str** |  | 
**timestamp** | **int** |  | 
**transactions** | [**List[Transaction]**](Transaction.md) |  | 
**receipts_root** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**parent_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**sha3_uncles** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**miner** | **str** | An ethereum address. | 
**state_root** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**transactions_root** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**logs_bloom** | **str** | A hex string. | 
**gas_used** | **int** |  | 
**nonce** | **str** | A hex string. | 
**mix_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**extra_data** | **bytearray** |  | 
**base_fee_per_gas** | **str** |  | [optional] 

## Example

```python
from multibaas_sdk.models.block import Block

# TODO update the JSON string below
json = "{}"
# create an instance of Block from a JSON string
block_instance = Block.from_json(json)
# print the JSON string representation of the object
print(Block.to_json())

# convert the object into a dict
block_dict = block_instance.to_dict()
# create an instance of Block from a dict
block_from_dict = Block.from_dict(block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


