# DeployContractTransaction

The transaction returned when you deploy a contracts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**TransactionToSignTx**](TransactionToSignTx.md) |  | 
**submitted** | **bool** |  | 
**deploy_at** | **str** |  | [optional] 
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | [optional] 

## Example

```python
from multibaas_sdk.models.deploy_contract_transaction import DeployContractTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of DeployContractTransaction from a JSON string
deploy_contract_transaction_instance = DeployContractTransaction.from_json(json)
# print the JSON string representation of the object
print(DeployContractTransaction.to_json())

# convert the object into a dict
deploy_contract_transaction_dict = deploy_contract_transaction_instance.to_dict()
# create an instance of DeployContractTransaction from a dict
deploy_contract_transaction_from_dict = DeployContractTransaction.from_dict(deploy_contract_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


