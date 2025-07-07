# PlanLimit

A limit on plan usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the limit. | 
**limit** | **int** | The limit value. Null means unlimited. | 
**count** | **int** | The current count for this limit. | [optional] 

## Example

```python
from multibaas_sdk.models.plan_limit import PlanLimit

# TODO update the JSON string below
json = "{}"
# create an instance of PlanLimit from a JSON string
plan_limit_instance = PlanLimit.from_json(json)
# print the JSON string representation of the object
print(PlanLimit.to_json())

# convert the object into a dict
plan_limit_dict = plan_limit_instance.to_dict()
# create an instance of PlanLimit from a dict
plan_limit_from_dict = PlanLimit.from_dict(plan_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


