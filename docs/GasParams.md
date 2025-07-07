# GasParams

Specify custom gas parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_price** | **str** | Gas price to use for the cancel/resubmit. | [optional] 
**gas_fee_cap** | **str** | Gas fee cap to use for the EIP-1559 cancel/resubmit. | [optional] 
**gas_tip_cap** | **str** | Gas priority fee cap to use for the EIP-1559 cancel/resubmit. | [optional] 
**gas** | **int** | Gas limit to set for the cancel/resubmit. | [optional] 

## Example

```python
from multibaas_sdk.models.gas_params import GasParams

# TODO update the JSON string below
json = "{}"
# create an instance of GasParams from a JSON string
gas_params_instance = GasParams.from_json(json)
# print the JSON string representation of the object
print(GasParams.to_json())

# convert the object into a dict
gas_params_dict = gas_params_instance.to_dict()
# create an instance of GasParams from a dict
gas_params_from_dict = GasParams.from_dict(gas_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


