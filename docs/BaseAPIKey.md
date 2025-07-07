# BaseAPIKey

An API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 

## Example

```python
from multibaas_sdk.models.base_api_key import BaseAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAPIKey from a JSON string
base_api_key_instance = BaseAPIKey.from_json(json)
# print the JSON string representation of the object
print(BaseAPIKey.to_json())

# convert the object into a dict
base_api_key_dict = base_api_key_instance.to_dict()
# create an instance of BaseAPIKey from a dict
base_api_key_from_dict = BaseAPIKey.from_dict(base_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


