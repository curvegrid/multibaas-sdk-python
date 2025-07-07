# StandaloneWallet

An object containing an HSM wallet's details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The Application ID that accesses the Key Vault. | [optional] 
**base_group_name** | **str** | The Resource Group Name for the resource being accessed. | 
**vault_name** | **str** | The name given to the vault your key is stored in. | [optional] 
**key_name** | **str** | The name of the key. | 
**key_version** | **str** | The version of the key. | [optional] 
**public_address** | **str** | An ethereum address. | 

## Example

```python
from multibaas_sdk.models.standalone_wallet import StandaloneWallet

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneWallet from a JSON string
standalone_wallet_instance = StandaloneWallet.from_json(json)
# print the JSON string representation of the object
print(StandaloneWallet.to_json())

# convert the object into a dict
standalone_wallet_dict = standalone_wallet_instance.to_dict()
# create an instance of StandaloneWallet from a dict
standalone_wallet_from_dict = StandaloneWallet.from_dict(standalone_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


