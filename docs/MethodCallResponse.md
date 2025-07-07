# MethodCallResponse

The result of a function call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **object** | The function call output. | 

## Example

```python
from multibaas_sdk.models.method_call_response import MethodCallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MethodCallResponse from a JSON string
method_call_response_instance = MethodCallResponse.from_json(json)
# print the JSON string representation of the object
print(MethodCallResponse.to_json())

# convert the object into a dict
method_call_response_dict = method_call_response_instance.to_dict()
# create an instance of MethodCallResponse from a dict
method_call_response_from_dict = MethodCallResponse.from_dict(method_call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


