# AzureAccount

An Azure account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**client_id** | **str** | The Application ID that will be accessing the Key Vault. | 
**client_secret** | **str** | The application’s secret key that you generate when you first register the application in Azure. | 
**tenant_id** | **str** | Also known as Directory ID. | 
**subscription_id** | **str** | The ID linked to your subscription to Azure services. | 
**base_group_name** | **str** | The Resource Group Name for the resource being accessed. | 
**id** | **int** |  | 

## Example

```python
from multibaas_sdk.models.azure_account import AzureAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AzureAccount from a JSON string
azure_account_instance = AzureAccount.from_json(json)
# print the JSON string representation of the object
print(AzureAccount.to_json())

# convert the object into a dict
azure_account_dict = azure_account_instance.to_dict()
# create an instance of AzureAccount from a dict
azure_account_from_dict = AzureAccount.from_dict(azure_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


