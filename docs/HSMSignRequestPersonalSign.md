# HSMSignRequestPersonalSign

Request to sign a message using a cloud wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The signing method to use. | 
**address** | **str** | An ethereum address. | 
**data** | **str** | A hex string. | 
**chain_id** | [**HSMSignRequestPersonalSignChainId**](HSMSignRequestPersonalSignChainId.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.hsm_sign_request_personal_sign import HSMSignRequestPersonalSign

# TODO update the JSON string below
json = "{}"
# create an instance of HSMSignRequestPersonalSign from a JSON string
hsm_sign_request_personal_sign_instance = HSMSignRequestPersonalSign.from_json(json)
# print the JSON string representation of the object
print(HSMSignRequestPersonalSign.to_json())

# convert the object into a dict
hsm_sign_request_personal_sign_dict = hsm_sign_request_personal_sign_instance.to_dict()
# create an instance of HSMSignRequestPersonalSign from a dict
hsm_sign_request_personal_sign_from_dict = HSMSignRequestPersonalSign.from_dict(hsm_sign_request_personal_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


