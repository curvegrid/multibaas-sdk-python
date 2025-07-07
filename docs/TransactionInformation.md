# TransactionInformation

The transaction information returned as part of an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | An ethereum address. | 
**tx_data** | **str** | A hex string. | 
**tx_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**tx_index_in_block** | **int** | The location of the transaction in the block. | 
**block_hash** | **str** | The keccak256 hash as a hex string of 256 bits. | 
**block_number** | **int** | The transaction block number. | 
**contract** | [**ContractInformation**](ContractInformation.md) |  | 
**method** | [**ContractMethodInformation**](ContractMethodInformation.md) |  | 

## Example

```python
from multibaas_sdk.models.transaction_information import TransactionInformation

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInformation from a JSON string
transaction_information_instance = TransactionInformation.from_json(json)
# print the JSON string representation of the object
print(TransactionInformation.to_json())

# convert the object into a dict
transaction_information_dict = transaction_information_instance.to_dict()
# create an instance of TransactionInformation from a dict
transaction_information_from_dict = TransactionInformation.from_dict(transaction_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


