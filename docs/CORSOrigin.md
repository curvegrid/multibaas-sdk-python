# CORSOrigin

CORS Origin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**origin** | **str** | The CORS Origin | [optional] 

## Example

```python
from multibaas_sdk.models.cors_origin import CORSOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of CORSOrigin from a JSON string
cors_origin_instance = CORSOrigin.from_json(json)
# print the JSON string representation of the object
print(CORSOrigin.to_json())

# convert the object into a dict
cors_origin_dict = cors_origin_instance.to_dict()
# create an instance of CORSOrigin from a dict
cors_origin_from_dict = CORSOrigin.from_dict(cors_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


