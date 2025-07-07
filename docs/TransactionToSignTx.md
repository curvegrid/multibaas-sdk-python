# TransactionToSignTx

An Ethereum transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **int** | Sender account nonce of the transaction | 
**gas_price** | **str** | Gas price of the transaction | [optional] 
**gas_fee_cap** | **str** | Fee cap per gas of the transaction | [optional] 
**gas_tip_cap** | **str** | GasTipCap per gas of the transaction | [optional] 
**gas** | **int** | Gas limit of the transaction | 
**var_from** | **str** | An ethereum address. | 
**to** | **str** | An ethereum address. | [optional] 
**value** | **str** | Amount (in wei) to send with the transaction. | 
**data** | **str** | A hex string. | 
**hash** | **str** | The keccak256 hash as a hex string of 256 bits. | [optional] 
**type** | **int** | Transaction type | 

## Example

```python
from multibaas_sdk.models.transaction_to_sign_tx import TransactionToSignTx

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionToSignTx from a JSON string
transaction_to_sign_tx_instance = TransactionToSignTx.from_json(json)
# print the JSON string representation of the object
print(TransactionToSignTx.to_json())

# convert the object into a dict
transaction_to_sign_tx_dict = transaction_to_sign_tx_instance.to_dict()
# create an instance of TransactionToSignTx from a dict
transaction_to_sign_tx_from_dict = TransactionToSignTx.from_dict(transaction_to_sign_tx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


