# AccessTuple

An access tuple representing an address and its storage keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An ethereum address. | 
**storage_keys** | **List[str]** |  | 

## Example

```python
from multibaas_sdk.models.access_tuple import AccessTuple

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTuple from a JSON string
access_tuple_instance = AccessTuple.from_json(json)
# print the JSON string representation of the object
print(AccessTuple.to_json())

# convert the object into a dict
access_tuple_dict = access_tuple_instance.to_dict()
# create an instance of AccessTuple from a dict
access_tuple_from_dict = AccessTuple.from_dict(access_tuple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


