# TransactionToSign

A transaction to be signed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**TransactionToSignTx**](TransactionToSignTx.md) |  | 
**submitted** | **bool** |  | 

## Example

```python
from multibaas_sdk.models.transaction_to_sign import TransactionToSign

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionToSign from a JSON string
transaction_to_sign_instance = TransactionToSign.from_json(json)
# print the JSON string representation of the object
print(TransactionToSign.to_json())

# convert the object into a dict
transaction_to_sign_dict = transaction_to_sign_instance.to_dict()
# create an instance of TransactionToSign from a dict
transaction_to_sign_from_dict = TransactionToSign.from_dict(transaction_to_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


