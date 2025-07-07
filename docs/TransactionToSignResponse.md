# TransactionToSignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**TransactionToSignTx**](TransactionToSignTx.md) |  | 
**submitted** | **bool** |  | 

## Example

```python
from multibaas_sdk.models.transaction_to_sign_response import TransactionToSignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionToSignResponse from a JSON string
transaction_to_sign_response_instance = TransactionToSignResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionToSignResponse.to_json())

# convert the object into a dict
transaction_to_sign_response_dict = transaction_to_sign_response_instance.to_dict()
# create an instance of TransactionToSignResponse from a dict
transaction_to_sign_response_from_dict = TransactionToSignResponse.from_dict(transaction_to_sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


