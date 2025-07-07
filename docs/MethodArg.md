# MethodArg

An argument passed to a method call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The input name. | 
**value** | **object** | The input value. | 
**type** | **str** | The type of the argument. | 

## Example

```python
from multibaas_sdk.models.method_arg import MethodArg

# TODO update the JSON string below
json = "{}"
# create an instance of MethodArg from a JSON string
method_arg_instance = MethodArg.from_json(json)
# print the JSON string representation of the object
print(MethodArg.to_json())

# convert the object into a dict
method_arg_dict = method_arg_instance.to_dict()
# create an instance of MethodArg from a dict
method_arg_from_dict = MethodArg.from_dict(method_arg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


