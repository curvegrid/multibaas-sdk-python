# HSMSignResponse

Response body representing a sign-data response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | 
**signature** | **str** |  | 

## Example

```python
from multibaas_sdk.models.hsm_sign_response import HSMSignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HSMSignResponse from a JSON string
hsm_sign_response_instance = HSMSignResponse.from_json(json)
# print the JSON string representation of the object
print(HSMSignResponse.to_json())

# convert the object into a dict
hsm_sign_response_dict = hsm_sign_response_instance.to_dict()
# create an instance of HSMSignResponse from a dict
hsm_sign_response_from_dict = HSMSignResponse.from_dict(hsm_sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


