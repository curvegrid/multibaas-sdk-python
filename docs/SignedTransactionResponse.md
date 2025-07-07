# SignedTransactionResponse

A transaction that was signed externally and submitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**Transaction**](Transaction.md) |  | 

## Example

```python
from multibaas_sdk.models.signed_transaction_response import SignedTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignedTransactionResponse from a JSON string
signed_transaction_response_instance = SignedTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(SignedTransactionResponse.to_json())

# convert the object into a dict
signed_transaction_response_dict = signed_transaction_response_instance.to_dict()
# create an instance of SignedTransactionResponse from a dict
signed_transaction_response_from_dict = SignedTransactionResponse.from_dict(signed_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


