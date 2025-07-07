# BaseUser

A user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email address. | 
**name** | **str** | The user&#39;s name. | 

## Example

```python
from multibaas_sdk.models.base_user import BaseUser

# TODO update the JSON string below
json = "{}"
# create an instance of BaseUser from a JSON string
base_user_instance = BaseUser.from_json(json)
# print the JSON string representation of the object
print(BaseUser.to_json())

# convert the object into a dict
base_user_dict = base_user_instance.to_dict()
# create an instance of BaseUser from a dict
base_user_from_dict = BaseUser.from_dict(base_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


