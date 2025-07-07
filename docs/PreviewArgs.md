# PreviewArgs

Ephemeral configuration for previewing the effect of a Type Conversion on a contract function call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs_only** | **bool** | Only preview the effect of a Type Conversion on the inputs. Only applicable for write function calls, where the output is an unsigned transaction. | 
**inputs** | [**List[ContractABIMethodArgument]**](ContractABIMethodArgument.md) | Type Conversion information for the function inputs. The number of inputs must match that of the actual function inputs. The parameter is a contract function argument where only the type conversion information is used. | 
**outputs** | [**List[ContractABIMethodArgument]**](ContractABIMethodArgument.md) | Type Conversion information for the function outputs. The number of outputs must match that of the actual function outputs. The parameter is a contract function argument where only the type conversion information is used. | 

## Example

```python
from multibaas_sdk.models.preview_args import PreviewArgs

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewArgs from a JSON string
preview_args_instance = PreviewArgs.from_json(json)
# print the JSON string representation of the object
print(PreviewArgs.to_json())

# convert the object into a dict
preview_args_dict = preview_args_instance.to_dict()
# create an instance of PreviewArgs from a dict
preview_args_from_dict = PreviewArgs.from_dict(preview_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


