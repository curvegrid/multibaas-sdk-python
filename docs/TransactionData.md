# TransactionData

The transaction data returned from a call to get transaction by hash.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Transaction**](Transaction.md) |  | 
**is_pending** | **bool** | Whether the transaction has been included yet. | 
**var_from** | **str** | An ethereum address. | 
**block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | [optional] 
**block_number** | **str** | The transaction block number. | [optional] 
**contract** | [**ContractInformation**](ContractInformation.md) |  | [optional] 
**method** | [**ContractMethodInformation**](ContractMethodInformation.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.transaction_data import TransactionData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionData from a JSON string
transaction_data_instance = TransactionData.from_json(json)
# print the JSON string representation of the object
print(TransactionData.to_json())

# convert the object into a dict
transaction_data_dict = transaction_data_instance.to_dict()
# create an instance of TransactionData from a dict
transaction_data_from_dict = TransactionData.from_dict(transaction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


