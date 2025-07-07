# SignData200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**HSMSignResponse**](HSMSignResponse.md) |  | 

## Example

```python
from multibaas_sdk.models.sign_data200_response import SignData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignData200Response from a JSON string
sign_data200_response_instance = SignData200Response.from_json(json)
# print the JSON string representation of the object
print(SignData200Response.to_json())

# convert the object into a dict
sign_data200_response_dict = sign_data200_response_instance.to_dict()
# create an instance of SignData200Response from a dict
sign_data200_response_from_dict = SignData200Response.from_dict(sign_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


