# AuthorizationExtraInfo

Additional information about any EIP-7702 authorizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority** | **str** | An ethereum address. | 
**format_valid** | **bool** | Indicates whether the format of the authorization is valid. | 
**notes** | **str** | Additional notes about the validity of the authorization. | 

## Example

```python
from multibaas_sdk.models.authorization_extra_info import AuthorizationExtraInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationExtraInfo from a JSON string
authorization_extra_info_instance = AuthorizationExtraInfo.from_json(json)
# print the JSON string representation of the object
print(AuthorizationExtraInfo.to_json())

# convert the object into a dict
authorization_extra_info_dict = authorization_extra_info_instance.to_dict()
# create an instance of AuthorizationExtraInfo from a dict
authorization_extra_info_from_dict = AuthorizationExtraInfo.from_dict(authorization_extra_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


