# PlanFeature

A feature flag in a plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the feature. | 
**enabled** | **bool** | Whether the feature is enabled. | 

## Example

```python
from multibaas_sdk.models.plan_feature import PlanFeature

# TODO update the JSON string below
json = "{}"
# create an instance of PlanFeature from a JSON string
plan_feature_instance = PlanFeature.from_json(json)
# print the JSON string representation of the object
print(PlanFeature.to_json())

# convert the object into a dict
plan_feature_dict = plan_feature_instance.to_dict()
# create an instance of PlanFeature from a dict
plan_feature_from_dict = PlanFeature.from_dict(plan_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


