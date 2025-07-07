# HSMSignRequestTypedData

Request to sign typed data using a cloud wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The signing method to use. | 
**address** | **str** | An ethereum address. | 
**data** | [**EIP712TypedData**](EIP712TypedData.md) |  | 

## Example

```python
from multibaas_sdk.models.hsm_sign_request_typed_data import HSMSignRequestTypedData

# TODO update the JSON string below
json = "{}"
# create an instance of HSMSignRequestTypedData from a JSON string
hsm_sign_request_typed_data_instance = HSMSignRequestTypedData.from_json(json)
# print the JSON string representation of the object
print(HSMSignRequestTypedData.to_json())

# convert the object into a dict
hsm_sign_request_typed_data_dict = hsm_sign_request_typed_data_instance.to_dict()
# create an instance of HSMSignRequestTypedData from a dict
hsm_sign_request_typed_data_from_dict = HSMSignRequestTypedData.from_dict(hsm_sign_request_typed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


