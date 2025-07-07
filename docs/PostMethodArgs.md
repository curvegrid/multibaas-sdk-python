# PostMethodArgs

Arguments to be passed into a contract function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** |  | [optional] 
**args** | **List[object]** | List of the function arguments. | [optional] 
**var_from** | **str** | An Ethereum address (0x prefixed hex) or an address alias. | [optional] 
**nonce** | **int** | Nonce to use for the transaction execution. | [optional] 
**gas_price** | **int** | Gas price to use for the transaction execution. | [optional] 
**gas_fee_cap** | **int** | Gas fee cap to use for the 1559 transaction execution. | [optional] 
**gas_tip_cap** | **int** | Gas priority fee cap to use for the 1559 transaction execution. | [optional] 
**gas** | **int** | Gas limit to set for the transaction execution. | [optional] 
**to** | **str** | An Ethereum address (0x prefixed hex) or an address alias. | [optional] 
**value** | **str** | Amount (in wei) to send with the transaction. | [optional] 
**sign_and_submit** | **bool** | If the &#x60;from&#x60; address is an HSM address and this flag is set to &#x60;true&#x60;, the transaction will be automatically signed and submitted to the blockchain. | [optional] [default to False]
**nonce_management** | **bool** | If the &#x60;from&#x60; address is an HSM address and this flag is set to &#x60;true&#x60;, MultiBaas will keep track of the nonce and set it accordingly. This is particularly useful when submitting multiple transactions concurrently or in a very short period of time. If this flag is set to &#x60;true&#x60; and a &#x60;nonce&#x60; is provided, it will reset the nonce tracker to the given nonce (useful if the nonce tracker is out of sync). | [optional] [default to False]
**pre_eip1559** | **bool** | If set to &#x60;true&#x60;, forces a legacy type transaction. Otherwise an EIP-1559 transaction will created if the network supports it. | [optional] [default to False]
**signer** | **str** | An Ethereum address (0x prefixed hex) or an address alias. | [optional] 
**format_ints** | **str** | Mode to format integer outputs in the function call&#39;s responses. There are 3 possible modes:   - &#x60;auto&#x60; (the default option), where number format is decided by its type:     - If the type has size at most 32 bits, then the number is returned verbatim.     - If the type has size larger than 32 bits, then the number is returned as a string.   - &#x60;as_numbers&#x60;, where all numbers are returned verbatim.   - &#x60;as_strings&#x60;, where all numbers are returned as strings.  | [optional] [default to 'auto']
**timestamp** | **str** | Call the function at a specific timestamp. Only available for read functions calls and if the &#x60;historical_blocks_feature&#x60; is enabled (see the plan endpoint). Mutually exclusive with the &#x60;blockNumber&#x60; parameter. | [optional] 
**block_number** | **str** | Call the function at a specific block. Only available for read functions calls and if the &#x60;historical_blocks_feature&#x60; is enabled (see the plan endpoint). Mutually exclusive with the &#x60;timestamp&#x60; parameter. | [optional] 
**contract_override** | **bool** | If set to true the given address and contract don&#39;t need to be linked for the function to be called. | [optional] 
**preview** | [**PreviewArgs**](PreviewArgs.md) |  | [optional] 

## Example

```python
from multibaas_sdk.models.post_method_args import PostMethodArgs

# TODO update the JSON string below
json = "{}"
# create an instance of PostMethodArgs from a JSON string
post_method_args_instance = PostMethodArgs.from_json(json)
# print the JSON string representation of the object
print(PostMethodArgs.to_json())

# convert the object into a dict
post_method_args_dict = post_method_args_instance.to_dict()
# create an instance of PostMethodArgs from a dict
post_method_args_from_dict = PostMethodArgs.from_dict(post_method_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


