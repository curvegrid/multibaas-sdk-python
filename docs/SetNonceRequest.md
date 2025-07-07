# SetNonceRequest

Request body representing a set local nonce request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** | If nonce is specified the provided value is set, otherwise the value is read from the blockchain. | [optional] 

## Example

```python
from multibaas_sdk.models.set_nonce_request import SetNonceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetNonceRequest from a JSON string
set_nonce_request_instance = SetNonceRequest.from_json(json)
# print the JSON string representation of the object
print(SetNonceRequest.to_json())

# convert the object into a dict
set_nonce_request_dict = set_nonce_request_instance.to_dict()
# create an instance of SetNonceRequest from a dict
set_nonce_request_from_dict = SetNonceRequest.from_dict(set_nonce_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


