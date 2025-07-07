# TransactionReceiptData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A hex string. | [optional] 
**root** | **str** | A hex string. | 
**status** | **str** | A hex string. | 
**cumulative_gas_used** | **str** | A hex string. | 
**logs_bloom** | **str** | A hex string. | 
**logs** | [**List[Log]**](Log.md) |  | 
**transaction_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**contract_address** | **str** | An ethereum address. | 
**gas_used** | **str** | A hex string. | 
**effective_gas_price** | **str** | A hex string. | 
**block_number** | **str** | A hex string. | 
**transaction_index** | **str** | A hex string. | 
**block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 

## Example

```python
from multibaas_sdk.models.transaction_receipt_data import TransactionReceiptData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReceiptData from a JSON string
transaction_receipt_data_instance = TransactionReceiptData.from_json(json)
# print the JSON string representation of the object
print(TransactionReceiptData.to_json())

# convert the object into a dict
transaction_receipt_data_dict = transaction_receipt_data_instance.to_dict()
# create an instance of TransactionReceiptData from a dict
transaction_receipt_data_from_dict = TransactionReceiptData.from_dict(transaction_receipt_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


