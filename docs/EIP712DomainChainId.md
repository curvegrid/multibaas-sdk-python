# EIP712DomainChainId

The EIP-155 chain ID of the application using the typed data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from multibaas_sdk.models.eip712_domain_chain_id import EIP712DomainChainId

# TODO update the JSON string below
json = "{}"
# create an instance of EIP712DomainChainId from a JSON string
eip712_domain_chain_id_instance = EIP712DomainChainId.from_json(json)
# print the JSON string representation of the object
print(EIP712DomainChainId.to_json())

# convert the object into a dict
eip712_domain_chain_id_dict = eip712_domain_chain_id_instance.to_dict()
# create an instance of EIP712DomainChainId from a dict
eip712_domain_chain_id_from_dict = EIP712DomainChainId.from_dict(eip712_domain_chain_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


