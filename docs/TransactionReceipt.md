# TransactionReceipt

Record of the transaction's outcome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionReceiptData**](TransactionReceiptData.md) |  | 
**events** | [**List[EventInformation]**](EventInformation.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.transaction_receipt import TransactionReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReceipt from a JSON string
transaction_receipt_instance = TransactionReceipt.from_json(json)
# print the JSON string representation of the object
print(TransactionReceipt.to_json())

# convert the object into a dict
transaction_receipt_dict = transaction_receipt_instance.to_dict()
# create an instance of TransactionReceipt from a dict
transaction_receipt_from_dict = TransactionReceipt.from_dict(transaction_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


