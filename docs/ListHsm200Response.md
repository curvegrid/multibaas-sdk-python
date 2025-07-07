# ListHsm200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**List[HSMData]**](HSMData.md) |  | 

## Example

```python
from multibaas_sdk.models.list_hsm200_response import ListHsm200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHsm200Response from a JSON string
list_hsm200_response_instance = ListHsm200Response.from_json(json)
# print the JSON string representation of the object
print(ListHsm200Response.to_json())

# convert the object into a dict
list_hsm200_response_dict = list_hsm200_response_instance.to_dict()
# create an instance of ListHsm200Response from a dict
list_hsm200_response_from_dict = ListHsm200Response.from_dict(list_hsm200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


