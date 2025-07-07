# WalletTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**Transaction**](Transaction.md) |  | 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**var_from** | **str** | An ethereum address. | 
**resubmission_attempts** | **int** | The total number of resubmission attempts. | 
**successful_resubmissions** | **int** | The total number of successful resubmission (added into the transaction pool). | 
**created_at** | **datetime** | The time the transaction was created. | 
**updated_at** | **datetime** | The time the transaction was last updated. | 
**failed** | **bool** | Whether the transaction failed when it was included in a block. | [optional] 
**block_number** | **int** | The block number that the transaction was included in. | [optional] 
**block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | [optional] 

## Example

```python
from multibaas_sdk.models.wallet_transaction import WalletTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of WalletTransaction from a JSON string
wallet_transaction_instance = WalletTransaction.from_json(json)
# print the JSON string representation of the object
print(WalletTransaction.to_json())

# convert the object into a dict
wallet_transaction_dict = wallet_transaction_instance.to_dict()
# create an instance of WalletTransaction from a dict
wallet_transaction_from_dict = WalletTransaction.from_dict(wallet_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


