# AddressAlias

An address and it's alias.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | An alias to easily identify and reference addresses. | 
**address** | **str** | An ethereum address. | 

## Example

```python
from multibaas_sdk.models.address_alias import AddressAlias

# TODO update the JSON string below
json = "{}"
# create an instance of AddressAlias from a JSON string
address_alias_instance = AddressAlias.from_json(json)
# print the JSON string representation of the object
print(AddressAlias.to_json())

# convert the object into a dict
address_alias_dict = address_alias_instance.to_dict()
# create an instance of AddressAlias from a dict
address_alias_from_dict = AddressAlias.from_dict(address_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


