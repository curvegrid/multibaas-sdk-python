# AddKey

Add key request data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The Application ID that will be accessing the Key Vault. | 
**key_name** | **str** | The name of the key. | 
**key_version** | **str** | The version of the key. | 
**vault_name** | **str** | The name given to the vault your key is stored in. | 

## Example

```python
from multibaas_sdk.models.add_key import AddKey

# TODO update the JSON string below
json = "{}"
# create an instance of AddKey from a JSON string
add_key_instance = AddKey.from_json(json)
# print the JSON string representation of the object
print(AddKey.to_json())

# convert the object into a dict
add_key_dict = add_key_instance.to_dict()
# create an instance of AddKey from a dict
add_key_from_dict = AddKey.from_dict(add_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


