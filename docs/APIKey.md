# APIKey

An API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**id** | **int** |  | 
**created_at** | **datetime** | The time the API key was created. | 
**last_used_at** | **datetime** | The time the API key was last used. | [optional] 
**created_by** | **int** | The ID of the user that created the API key. | 
**signature** | **str** | The signature of the API key. | 

## Example

```python
from multibaas_sdk.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print(APIKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_from_dict = APIKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


