# ListContractVersions200ResponseAllOfResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**versions** | **List[str]** |  | 

## Example

```python
from multibaas_sdk.models.list_contract_versions200_response_all_of_result import ListContractVersions200ResponseAllOfResult

# TODO update the JSON string below
json = "{}"
# create an instance of ListContractVersions200ResponseAllOfResult from a JSON string
list_contract_versions200_response_all_of_result_instance = ListContractVersions200ResponseAllOfResult.from_json(json)
# print the JSON string representation of the object
print(ListContractVersions200ResponseAllOfResult.to_json())

# convert the object into a dict
list_contract_versions200_response_all_of_result_dict = list_contract_versions200_response_all_of_result_instance.to_dict()
# create an instance of ListContractVersions200ResponseAllOfResult from a dict
list_contract_versions200_response_all_of_result_from_dict = ListContractVersions200ResponseAllOfResult.from_dict(list_contract_versions200_response_all_of_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


