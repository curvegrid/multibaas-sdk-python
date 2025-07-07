# CreateKey

Create Key request data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The Application ID that will be accessing the Key Vault. | 
**key_name** | **str** | The name of the key. | 
**vault_name** | **str** | The name given to the vault your key is stored in. | 
**use_hardware_module** | **bool** |  | 

## Example

```python
from multibaas_sdk.models.create_key import CreateKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKey from a JSON string
create_key_instance = CreateKey.from_json(json)
# print the JSON string representation of the object
print(CreateKey.to_json())

# convert the object into a dict
create_key_dict = create_key_instance.to_dict()
# create an instance of CreateKey from a dict
create_key_from_dict = CreateKey.from_dict(create_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


