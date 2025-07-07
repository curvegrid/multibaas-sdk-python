# GetChainStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**ChainStatus**](ChainStatus.md) |  | 

## Example

```python
from multibaas_sdk.models.get_chain_status200_response import GetChainStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetChainStatus200Response from a JSON string
get_chain_status200_response_instance = GetChainStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetChainStatus200Response.to_json())

# convert the object into a dict
get_chain_status200_response_dict = get_chain_status200_response_instance.to_dict()
# create an instance of GetChainStatus200Response from a dict
get_chain_status200_response_from_dict = GetChainStatus200Response.from_dict(get_chain_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


