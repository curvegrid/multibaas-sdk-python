# SetCodeAuthorization

Authorization data for setCode operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | A hex string. | 
**address** | **str** | An ethereum address. | 
**nonce** | **str** | A hex string. | 
**y_parity** | **str** | A hex string. | 
**r** | **str** | A hex string. | 
**s** | **str** | A hex string. | 

## Example

```python
from multibaas_sdk.models.set_code_authorization import SetCodeAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of SetCodeAuthorization from a JSON string
set_code_authorization_instance = SetCodeAuthorization.from_json(json)
# print the JSON string representation of the object
print(SetCodeAuthorization.to_json())

# convert the object into a dict
set_code_authorization_dict = set_code_authorization_instance.to_dict()
# create an instance of SetCodeAuthorization from a dict
set_code_authorization_from_dict = SetCodeAuthorization.from_dict(set_code_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


