# ListHsmWallets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**List[StandaloneWallet]**](StandaloneWallet.md) |  | 

## Example

```python
from multibaas_sdk.models.list_hsm_wallets200_response import ListHsmWallets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHsmWallets200Response from a JSON string
list_hsm_wallets200_response_instance = ListHsmWallets200Response.from_json(json)
# print the JSON string representation of the object
print(ListHsmWallets200Response.to_json())

# convert the object into a dict
list_hsm_wallets200_response_dict = list_hsm_wallets200_response_instance.to_dict()
# create an instance of ListHsmWallets200Response from a dict
list_hsm_wallets200_response_from_dict = ListHsmWallets200Response.from_dict(list_hsm_wallets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


