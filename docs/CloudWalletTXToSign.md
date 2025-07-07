# CloudWalletTXToSign

A Cloud Wallet transaction to be signed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**CloudWalletTXToSignTx**](CloudWalletTXToSignTx.md) |  | 

## Example

```python
from multibaas_sdk.models.cloud_wallet_txto_sign import CloudWalletTXToSign

# TODO update the JSON string below
json = "{}"
# create an instance of CloudWalletTXToSign from a JSON string
cloud_wallet_txto_sign_instance = CloudWalletTXToSign.from_json(json)
# print the JSON string representation of the object
print(CloudWalletTXToSign.to_json())

# convert the object into a dict
cloud_wallet_txto_sign_dict = cloud_wallet_txto_sign_instance.to_dict()
# create an instance of CloudWalletTXToSign from a dict
cloud_wallet_txto_sign_from_dict = CloudWalletTXToSign.from_dict(cloud_wallet_txto_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


