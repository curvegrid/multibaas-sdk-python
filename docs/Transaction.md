# Transaction

A transaction from the Ethereum Blockchain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A hex string. | 
**chain_id** | **str** | A hex string or null. | [optional] 
**nonce** | **str** | A hex string. | 
**to** | **str** | An ethereum address. | 
**var_from** | **str** | An ethereum address. | [optional] 
**gas** | **str** | A hex string. | 
**gas_price** | **str** | A hex string or null. | [optional] 
**max_priority_fee_per_gas** | **str** | A hex string or null. | [optional] 
**max_fee_per_gas** | **str** | A hex string or null. | [optional] 
**max_fee_per_blob_gas** | **str** | A hex string or null. | [optional] 
**value** | **str** | A hex string or null. | 
**input** | **str** | A hex string. | 
**access_list** | [**List[AccessTuple]**](AccessTuple.md) |  | [optional] 
**blob_versioned_hashes** | **List[str]** |  | [optional] 
**authorization_list** | [**List[SetCodeAuthorization]**](SetCodeAuthorization.md) |  | [optional] 
**v** | **str** | A hex string. | 
**r** | **str** | A hex string. | 
**s** | **str** | A hex string. | 
**y_parity** | **str** | A hex string or null. | [optional] 
**blobs** | **List[str]** |  | [optional] 
**commitments** | **List[str]** |  | [optional] 
**proofs** | **List[str]** |  | [optional] 
**hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 

## Example

```python
from multibaas_sdk.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


