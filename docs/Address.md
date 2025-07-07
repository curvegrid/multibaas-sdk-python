# Address

An address details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | An alias to easily identify and reference addresses. | 
**address** | **str** | An ethereum address. | 
**balance** | **str** |  | [optional] 
**chain** | **str** |  | 
**nonce** | **int** | The next transaction nonce for this address (obtained from the blockchain node). | [optional] 
**local_nonce** | **int** | The next transaction nonce for this address when using the nonce management feature. | [optional] 
**code_at** | **bytearray** |  | [optional] 
**contracts** | [**List[ContractMetadata]**](ContractMetadata.md) |  | 
**contract_lookup** | [**List[ContractLookup]**](ContractLookup.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


