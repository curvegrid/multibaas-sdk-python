# SubmitSignedTransaction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**SignedTransactionResponse**](SignedTransactionResponse.md) |  | 

## Example

```python
from multibaas_sdk.models.submit_signed_transaction200_response import SubmitSignedTransaction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitSignedTransaction200Response from a JSON string
submit_signed_transaction200_response_instance = SubmitSignedTransaction200Response.from_json(json)
# print the JSON string representation of the object
print(SubmitSignedTransaction200Response.to_json())

# convert the object into a dict
submit_signed_transaction200_response_dict = submit_signed_transaction200_response_instance.to_dict()
# create an instance of SubmitSignedTransaction200Response from a dict
submit_signed_transaction200_response_from_dict = SubmitSignedTransaction200Response.from_dict(submit_signed_transaction200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


