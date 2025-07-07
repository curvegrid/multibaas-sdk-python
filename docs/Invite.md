# Invite

A user invitation to MultiBaas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invite ID. | 
**email** | **str** | The invitee&#39;s email address. | 
**created_at** | **datetime** | The time the invite was created. | 

## Example

```python
from multibaas_sdk.models.invite import Invite

# TODO update the JSON string below
json = "{}"
# create an instance of Invite from a JSON string
invite_instance = Invite.from_json(json)
# print the JSON string representation of the object
print(Invite.to_json())

# convert the object into a dict
invite_dict = invite_instance.to_dict()
# create an instance of Invite from a dict
invite_from_dict = Invite.from_dict(invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


