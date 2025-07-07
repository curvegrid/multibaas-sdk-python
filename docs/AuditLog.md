# AuditLog

An audit log entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_by_id** | **int** | The ID of the user who performed the action. | 
**action_on_id** | **int** | The ID of the user who was acted upon. | [optional] 
**action_by_user_email** | **str** | The email of the user who performed the action. | 
**action_on_user_email** | **str** | The email of the user who was acted upon. | [optional] 
**type** | **str** | The type of action that was performed. | 
**created_at** | **datetime** | The time the action was performed. | 
**activity_data** | **object** | The data associated with the action. | 

## Example

```python
from multibaas_sdk.models.audit_log import AuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLog from a JSON string
audit_log_instance = AuditLog.from_json(json)
# print the JSON string representation of the object
print(AuditLog.to_json())

# convert the object into a dict
audit_log_dict = audit_log_instance.to_dict()
# create an instance of AuditLog from a dict
audit_log_from_dict = AuditLog.from_dict(audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


