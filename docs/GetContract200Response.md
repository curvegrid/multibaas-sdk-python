# GetContract200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**Contract**](Contract.md) |  | 

## Example

```python
from multibaas_sdk.models.get_contract200_response import GetContract200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContract200Response from a JSON string
get_contract200_response_instance = GetContract200Response.from_json(json)
# print the JSON string representation of the object
print(GetContract200Response.to_json())

# convert the object into a dict
get_contract200_response_dict = get_contract200_response_instance.to_dict()
# create an instance of GetContract200Response from a dict
get_contract200_response_from_dict = GetContract200Response.from_dict(get_contract200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


