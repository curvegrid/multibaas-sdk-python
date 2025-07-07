# LinkAddressContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An alias to easily identify and reference the entity in subsequent requests. | 
**version** | **str** | The contract version. | [optional] 
**starting_block** | **str** | The block number from which to start syncing events. The value can be &#x60;latest&#x60; for the latest block number, an absolute block number (e.g. &#x60;123&#x60; for the block number 123), or a relative block number (e.g. &#x60;-100&#x60; for 100 blocks before the latest block). If absent, the event monitor will be disabled for this contract and events won&#39;t be synced. | [optional] 

## Example

```python
from multibaas_sdk.models.link_address_contract_request import LinkAddressContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAddressContractRequest from a JSON string
link_address_contract_request_instance = LinkAddressContractRequest.from_json(json)
# print the JSON string representation of the object
print(LinkAddressContractRequest.to_json())

# convert the object into a dict
link_address_contract_request_dict = link_address_contract_request_instance.to_dict()
# create an instance of LinkAddressContractRequest from a dict
link_address_contract_request_from_dict = LinkAddressContractRequest.from_dict(link_address_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


