# DeployContract200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**DeployContractTransaction**](DeployContractTransaction.md) |  | 

## Example

```python
from multibaas_sdk.models.deploy_contract200_response import DeployContract200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeployContract200Response from a JSON string
deploy_contract200_response_instance = DeployContract200Response.from_json(json)
# print the JSON string representation of the object
print(DeployContract200Response.to_json())

# convert the object into a dict
deploy_contract200_response_dict = deploy_contract200_response_instance.to_dict()
# create an instance of DeployContract200Response from a dict
deploy_contract200_response_from_dict = DeployContract200Response.from_dict(deploy_contract200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


