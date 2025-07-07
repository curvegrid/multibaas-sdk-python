# MethodCallPreviewResponse

The result of a preview function arguments call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **List[object]** | The function call inputs. | 
**output** | **object** | The function call output. | 

## Example

```python
from multibaas_sdk.models.method_call_preview_response import MethodCallPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MethodCallPreviewResponse from a JSON string
method_call_preview_response_instance = MethodCallPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(MethodCallPreviewResponse.to_json())

# convert the object into a dict
method_call_preview_response_dict = method_call_preview_response_instance.to_dict()
# create an instance of MethodCallPreviewResponse from a dict
method_call_preview_response_from_dict = MethodCallPreviewResponse.from_dict(method_call_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


