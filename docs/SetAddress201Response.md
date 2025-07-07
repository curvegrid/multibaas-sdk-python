# SetAddress201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**Address**](Address.md) |  | 

## Example

```python
from multibaas_sdk.models.set_address201_response import SetAddress201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetAddress201Response from a JSON string
set_address201_response_instance = SetAddress201Response.from_json(json)
# print the JSON string representation of the object
print(SetAddress201Response.to_json())

# convert the object into a dict
set_address201_response_dict = set_address201_response_instance.to_dict()
# create an instance of SetAddress201Response from a dict
set_address201_response_from_dict = SetAddress201Response.from_dict(set_address201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


