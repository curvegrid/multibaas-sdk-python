# ListAuditLogs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The status code. | 
**message** | **str** | The human-readable status message. | 
**result** | [**List[AuditLog]**](AuditLog.md) |  | 

## Example

```python
from multibaas_sdk.models.list_audit_logs200_response import ListAuditLogs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuditLogs200Response from a JSON string
list_audit_logs200_response_instance = ListAuditLogs200Response.from_json(json)
# print the JSON string representation of the object
print(ListAuditLogs200Response.to_json())

# convert the object into a dict
list_audit_logs200_response_dict = list_audit_logs200_response_instance.to_dict()
# create an instance of ListAuditLogs200Response from a dict
list_audit_logs200_response_from_dict = ListAuditLogs200Response.from_dict(list_audit_logs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


