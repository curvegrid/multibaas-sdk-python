# SignedTransactionSubmission

The object used to receive a pre-signed raw transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** | The pre-signed raw transaction. | 

## Example

```python
from multibaas_sdk.models.signed_transaction_submission import SignedTransactionSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of SignedTransactionSubmission from a JSON string
signed_transaction_submission_instance = SignedTransactionSubmission.from_json(json)
# print the JSON string representation of the object
print(SignedTransactionSubmission.to_json())

# convert the object into a dict
signed_transaction_submission_dict = signed_transaction_submission_instance.to_dict()
# create an instance of SignedTransactionSubmission from a dict
signed_transaction_submission_from_dict = SignedTransactionSubmission.from_dict(signed_transaction_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


