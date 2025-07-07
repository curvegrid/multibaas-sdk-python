# HSMSignRequestPersonalSignChainId

Optionally lock the message to a specific chain by encoding the chain ID in the signature per EIP-155.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from multibaas_sdk.models.hsm_sign_request_personal_sign_chain_id import HSMSignRequestPersonalSignChainId

# TODO update the JSON string below
json = "{}"
# create an instance of HSMSignRequestPersonalSignChainId from a JSON string
hsm_sign_request_personal_sign_chain_id_instance = HSMSignRequestPersonalSignChainId.from_json(json)
# print the JSON string representation of the object
print(HSMSignRequestPersonalSignChainId.to_json())

# convert the object into a dict
hsm_sign_request_personal_sign_chain_id_dict = hsm_sign_request_personal_sign_chain_id_instance.to_dict()
# create an instance of HSMSignRequestPersonalSignChainId from a dict
hsm_sign_request_personal_sign_chain_id_from_dict = HSMSignRequestPersonalSignChainId.from_dict(hsm_sign_request_personal_sign_chain_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


