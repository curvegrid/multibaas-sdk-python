# AzureWallet

An HSM Wallet returned when a new key is created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | The name of the key. | 
**key_version** | **str** | The version of the key. | 
**public_address** | **str** | An ethereum address. | 

## Example

```python
from multibaas_sdk.models.azure_wallet import AzureWallet

# TODO update the JSON string below
json = "{}"
# create an instance of AzureWallet from a JSON string
azure_wallet_instance = AzureWallet.from_json(json)
# print the JSON string representation of the object
print(AzureWallet.to_json())

# convert the object into a dict
azure_wallet_dict = azure_wallet_instance.to_dict()
# create an instance of AzureWallet from a dict
azure_wallet_from_dict = AzureWallet.from_dict(azure_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


