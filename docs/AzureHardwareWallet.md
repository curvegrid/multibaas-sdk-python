# AzureHardwareWallet

An HSM Wallet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**azure_account_id** | **int** |  | 
**vault_name** | **str** | The name given to the vault your key is stored in. | 
**key_name** | **str** | The name of the key. | 
**key_version** | **str** | The version of the key. | 
**public_address** | **str** | An ethereum address. | 

## Example

```python
from multibaas_sdk.models.azure_hardware_wallet import AzureHardwareWallet

# TODO update the JSON string below
json = "{}"
# create an instance of AzureHardwareWallet from a JSON string
azure_hardware_wallet_instance = AzureHardwareWallet.from_json(json)
# print the JSON string representation of the object
print(AzureHardwareWallet.to_json())

# convert the object into a dict
azure_hardware_wallet_dict = azure_hardware_wallet_instance.to_dict()
# create an instance of AzureHardwareWallet from a dict
azure_hardware_wallet_from_dict = AzureHardwareWallet.from_dict(azure_hardware_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


