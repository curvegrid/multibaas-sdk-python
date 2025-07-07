# EIP712TypedData

EIP-712 structured typed data object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**EIP712Types**](EIP712Types.md) |  | 
**primary_type** | **str** | The root type of the message object. Must correspond to a key in the &#x60;types&#x60; object. | 
**domain** | [**EIP712Domain**](EIP712Domain.md) |  | 
**message** | **object** | The actual data, conforming to the &#x60;primaryType&#x60; definition in &#x60;types&#x60;. | 

## Example

```python
from multibaas_sdk.models.eip712_typed_data import EIP712TypedData

# TODO update the JSON string below
json = "{}"
# create an instance of EIP712TypedData from a JSON string
eip712_typed_data_instance = EIP712TypedData.from_json(json)
# print the JSON string representation of the object
print(EIP712TypedData.to_json())

# convert the object into a dict
eip712_typed_data_dict = eip712_typed_data_instance.to_dict()
# create an instance of EIP712TypedData from a dict
eip712_typed_data_from_dict = EIP712TypedData.from_dict(eip712_typed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


