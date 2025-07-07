# Plan

A plan containing limits and features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the plan. | 
**updated_at** | **str** | When the plan was last updated. | 
**limits** | [**List[PlanLimit]**](PlanLimit.md) | The limits associated with the plan. | 
**features** | [**List[PlanFeature]**](PlanFeature.md) | The features associated with the plan. | 

## Example

```python
from multibaas_sdk.models.plan import Plan

# TODO update the JSON string below
json = "{}"
# create an instance of Plan from a JSON string
plan_instance = Plan.from_json(json)
# print the JSON string representation of the object
print(Plan.to_json())

# convert the object into a dict
plan_dict = plan_instance.to_dict()
# create an instance of Plan from a dict
plan_from_dict = Plan.from_dict(plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


