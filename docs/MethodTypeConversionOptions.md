# MethodTypeConversionOptions

Type conversion options for each of the inputs and outputs of a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[TypeConversionOptions]**](TypeConversionOptions.md) |  | 
**outputs** | [**List[TypeConversionOptions]**](TypeConversionOptions.md) |  | 

## Example

```python
from multibaas_sdk.models.method_type_conversion_options import MethodTypeConversionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MethodTypeConversionOptions from a JSON string
method_type_conversion_options_instance = MethodTypeConversionOptions.from_json(json)
# print the JSON string representation of the object
print(MethodTypeConversionOptions.to_json())

# convert the object into a dict
method_type_conversion_options_dict = method_type_conversion_options_instance.to_dict()
# create an instance of MethodTypeConversionOptions from a dict
method_type_conversion_options_from_dict = MethodTypeConversionOptions.from_dict(method_type_conversion_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


