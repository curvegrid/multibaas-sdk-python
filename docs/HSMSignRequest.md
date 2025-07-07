# HSMSignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The signing method to use. | 
**address** | **str** | An ethereum address. | 
**data** | [**EIP712TypedData**](EIP712TypedData.md) |  | 
**chain_id** | [**HSMSignRequestPersonalSignChainId**](HSMSignRequestPersonalSignChainId.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.hsm_sign_request import HSMSignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HSMSignRequest from a JSON string
hsm_sign_request_instance = HSMSignRequest.from_json(json)
# print the JSON string representation of the object
print(HSMSignRequest.to_json())

# convert the object into a dict
hsm_sign_request_dict = hsm_sign_request_instance.to_dict()
# create an instance of HSMSignRequest from a dict
hsm_sign_request_from_dict = HSMSignRequest.from_dict(hsm_sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


