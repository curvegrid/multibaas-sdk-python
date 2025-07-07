# SignerWallet

A signer wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the signer. | 
**wallet** | **str** | An ethereum address. | 
**signer** | **str** | An ethereum address. | 
**label** | **str** | The label of the signer. | 

## Example

```python
from multibaas_sdk.models.signer_wallet import SignerWallet

# TODO update the JSON string below
json = "{}"
# create an instance of SignerWallet from a JSON string
signer_wallet_instance = SignerWallet.from_json(json)
# print the JSON string representation of the object
print(SignerWallet.to_json())

# convert the object into a dict
signer_wallet_dict = signer_wallet_instance.to_dict()
# create an instance of SignerWallet from a dict
signer_wallet_from_dict = SignerWallet.from_dict(signer_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


