# TransferEth200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**TransactionToSign**](TransactionToSign.md) |  | 

## Example

```python
from multibaas_sdk.models.transfer_eth200_response import TransferEth200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEth200Response from a JSON string
transfer_eth200_response_instance = TransferEth200Response.from_json(json)
# print the JSON string representation of the object
print(TransferEth200Response.to_json())

# convert the object into a dict
transfer_eth200_response_dict = transfer_eth200_response_instance.to_dict()
# create an instance of TransferEth200Response from a dict
transfer_eth200_response_from_dict = TransferEth200Response.from_dict(transfer_eth200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


