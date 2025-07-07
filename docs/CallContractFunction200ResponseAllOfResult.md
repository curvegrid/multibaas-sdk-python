# CallContractFunction200ResponseAllOfResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The response object type (discriminator). | 
**output** | **object** | The function call output. | 
**input** | **List[object]** | The function call inputs. | 

## Example

```python
from multibaas_sdk.models.call_contract_function200_response_all_of_result import CallContractFunction200ResponseAllOfResult

# TODO update the JSON string below
json = "{}"
# create an instance of CallContractFunction200ResponseAllOfResult from a JSON string
call_contract_function200_response_all_of_result_instance = CallContractFunction200ResponseAllOfResult.from_json(json)
# print the JSON string representation of the object
print(CallContractFunction200ResponseAllOfResult.to_json())

# convert the object into a dict
call_contract_function200_response_all_of_result_dict = call_contract_function200_response_all_of_result_instance.to_dict()
# create an instance of CallContractFunction200ResponseAllOfResult from a dict
call_contract_function200_response_all_of_result_from_dict = CallContractFunction200ResponseAllOfResult.from_dict(call_contract_function200_response_all_of_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


