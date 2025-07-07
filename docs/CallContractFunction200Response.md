# CallContractFunction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**CallContractFunction200ResponseAllOfResult**](CallContractFunction200ResponseAllOfResult.md) |  | 

## Example

```python
from multibaas_sdk.models.call_contract_function200_response import CallContractFunction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CallContractFunction200Response from a JSON string
call_contract_function200_response_instance = CallContractFunction200Response.from_json(json)
# print the JSON string representation of the object
print(CallContractFunction200Response.to_json())

# convert the object into a dict
call_contract_function200_response_dict = call_contract_function200_response_instance.to_dict()
# create an instance of CallContractFunction200Response from a dict
call_contract_function200_response_from_dict = CallContractFunction200Response.from_dict(call_contract_function200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


