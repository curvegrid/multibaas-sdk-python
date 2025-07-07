# HSMData

Response body for returning HSM Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**AzureAccount**](AzureAccount.md) |  | 
**wallets** | [**List[AzureHardwareWallet]**](AzureHardwareWallet.md) | An array of Azure Hardware Wallets. | 

## Example

```python
from multibaas_sdk.models.hsm_data import HSMData

# TODO update the JSON string below
json = "{}"
# create an instance of HSMData from a JSON string
hsm_data_instance = HSMData.from_json(json)
# print the JSON string representation of the object
print(HSMData.to_json())

# convert the object into a dict
hsm_data_dict = hsm_data_instance.to_dict()
# create an instance of HSMData from a dict
hsm_data_from_dict = HSMData.from_dict(hsm_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


