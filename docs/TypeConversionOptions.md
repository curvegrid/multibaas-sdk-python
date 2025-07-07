# TypeConversionOptions

Represents the set of type conversions allowed for a particular input or output of a function (how it may be \"cast\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **List[str]** |  | [optional] 

## Example

```python
from multibaas_sdk.models.type_conversion_options import TypeConversionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TypeConversionOptions from a JSON string
type_conversion_options_instance = TypeConversionOptions.from_json(json)
# print the JSON string representation of the object
print(TypeConversionOptions.to_json())

# convert the object into a dict
type_conversion_options_dict = type_conversion_options_instance.to_dict()
# create an instance of TypeConversionOptions from a dict
type_conversion_options_from_dict = TypeConversionOptions.from_dict(type_conversion_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


