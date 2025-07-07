# SignerLabel

A signer label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the signer. | 

## Example

```python
from multibaas_sdk.models.signer_label import SignerLabel

# TODO update the JSON string below
json = "{}"
# create an instance of SignerLabel from a JSON string
signer_label_instance = SignerLabel.from_json(json)
# print the JSON string representation of the object
print(SignerLabel.to_json())

# convert the object into a dict
signer_label_dict = signer_label_instance.to_dict()
# create an instance of SignerLabel from a dict
signer_label_from_dict = SignerLabel.from_dict(signer_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


