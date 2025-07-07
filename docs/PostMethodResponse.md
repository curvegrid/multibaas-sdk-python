# PostMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The response object type (discriminator). | 

## Example

```python
from multibaas_sdk.models.post_method_response import PostMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostMethodResponse from a JSON string
post_method_response_instance = PostMethodResponse.from_json(json)
# print the JSON string representation of the object
print(PostMethodResponse.to_json())

# convert the object into a dict
post_method_response_dict = post_method_response_instance.to_dict()
# create an instance of PostMethodResponse from a dict
post_method_response_from_dict = PostMethodResponse.from_dict(post_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


