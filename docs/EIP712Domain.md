# EIP712Domain

The domain fields for EIP-712. All fields are optional per the specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the signing domain. | [optional] 
**version** | **str** | Current major version of the signing domain. | [optional] 
**chain_id** | [**EIP712DomainChainId**](EIP712DomainChainId.md) |  | [optional] 
**verifying_contract** | **str** | An ethereum address. | [optional] 
**salt** | **str** | A hex string. | [optional] 

## Example

```python
from multibaas_sdk.models.eip712_domain import EIP712Domain

# TODO update the JSON string below
json = "{}"
# create an instance of EIP712Domain from a JSON string
eip712_domain_instance = EIP712Domain.from_json(json)
# print the JSON string representation of the object
print(EIP712Domain.to_json())

# convert the object into a dict
eip712_domain_dict = eip712_domain_instance.to_dict()
# create an instance of EIP712Domain from a dict
eip712_domain_from_dict = EIP712Domain.from_dict(eip712_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


