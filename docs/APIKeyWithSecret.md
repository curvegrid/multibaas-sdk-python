# APIKeyWithSecret

A freshly created API key with its secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**id** | **int** |  | 
**created_at** | **datetime** | The time the API key was created. | 
**last_used_at** | **datetime** | The time the API key was last used. | [optional] 
**created_by** | **int** | The ID of the user that created the API key. | 
**signature** | **str** | The signature of the API key. | 
**key** | **str** | The secret key of the API key. | 

## Example

```python
from multibaas_sdk.models.api_key_with_secret import APIKeyWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyWithSecret from a JSON string
api_key_with_secret_instance = APIKeyWithSecret.from_json(json)
# print the JSON string representation of the object
print(APIKeyWithSecret.to_json())

# convert the object into a dict
api_key_with_secret_dict = api_key_with_secret_instance.to_dict()
# create an instance of APIKeyWithSecret from a dict
api_key_with_secret_from_dict = APIKeyWithSecret.from_dict(api_key_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


