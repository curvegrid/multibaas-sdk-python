# AcceptInvite200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**User**](User.md) |  | 

## Example

```python
from multibaas_sdk.models.accept_invite200_response import AcceptInvite200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptInvite200Response from a JSON string
accept_invite200_response_instance = AcceptInvite200Response.from_json(json)
# print the JSON string representation of the object
print(AcceptInvite200Response.to_json())

# convert the object into a dict
accept_invite200_response_dict = accept_invite200_response_instance.to_dict()
# create an instance of AcceptInvite200Response from a dict
accept_invite200_response_from_dict = AcceptInvite200Response.from_dict(accept_invite200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


