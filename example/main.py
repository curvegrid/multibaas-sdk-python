#!/usr/bin/env python
# coding: utf-8

"""
Example script for using the MultiBaas Python SDK.
"""

import os
from urllib.parse import urljoin
from dotenv import load_dotenv

import multibaas_sdk
from multibaas_sdk.configuration import Configuration
from multibaas_sdk.api.chains_api import ChainsApi
from multibaas_sdk.api.contracts_api import ContractsApi
from multibaas_sdk.models.post_method_args import PostMethodArgs
from multibaas_sdk.exceptions import ApiException

# Load environment variables from .env file
load_dotenv()

# chainID to ERC20 contract address mapping for examples
CHAIN_ID_TO_ERC20_ADDR = {
    1: "0x6B175474E89094C44Da98b954EedeAC495271d0F",  # Ethereum Mainnet
    5: "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6",  # Ethereum Goerli
    11155111: "0x969D499507B4f437953Db24A4980FdEEDa6Db8a1",  # Ethereum Sepolia
    137: "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",  # Polygon Mainnet
    80001: "0x3C0d2375d317092F530caFb440337b4E88163f29",  # Polygon Mumbai
    43114: "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70",  # Avalanche Mainnet
    43113: "0x12C135a68b7B3Cd006eDb785cB53398a5DA59613",  # Avalanche Fuji
    2017072401: "0x8a58447d8AE49b6Ac6cf773B11a3981C46a6D89D"  # Curvegrid Testnet
}


def main():
    """
    Main function demonstrating MultiBaas SDK usage.
    """
    # Initialize the SDK using environment variables
    base_path = urljoin(os.getenv("MB_BASE_URL"), "/api/v0")
    config = Configuration(
        host=base_path,
        access_token=os.getenv("MB_API_KEY")
    )

    chain = "ethereum"

    # Example 1: Getting blockchain details
    try:
        # First get the chain ID of the blockchain MultiBaas is connected to
        chains_api = ChainsApi(api_client=multibaas_sdk.ApiClient(config))
        resp1 = chains_api.get_chain_status(chain)
        
        chain_id = resp1.result.chain_id
        latest_block = resp1.result.block_number
        
        print(
            f"Example 1: MultiBaas is connected to the chain ID #{chain_id} "
            f"and the latest block number is #{latest_block}"
        )
        
        # Example 2: Calling a smart contract function
        wallet_addr = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"  # Vitalik Buterin's wallet
        contract_label = "erc20interface"
        contract_method = "balanceOf"
        
        contract_addr = CHAIN_ID_TO_ERC20_ADDR.get(chain_id)
        if contract_addr is None:
            raise ValueError(f"This code example is missing an ERC20 contract address for the chain ID {chain_id}")
        
        payload = PostMethodArgs(
            args=[wallet_addr],
            contract_override=True
        )
        
        contracts_api = ContractsApi(api_client=multibaas_sdk.ApiClient(config))
        resp2 = contracts_api.call_contract_function(
            chain, contract_addr, contract_label, contract_method, post_method_args=payload
        )
                
        # Use the to_dict() method to access the underlying response data
        result_dict = resp2.result.to_dict()
        if result_dict.get('kind') == "MethodCallResponse":
            balance = result_dict.get('output')
            print(
                f"Example 2: The wallet {wallet_addr} balance on the "
                f"ERC20 contract {contract_addr} is: {balance}"
            )
        else:
            raise ValueError(f"Example 2: Unexpected response type: {result_dict.get('kind')}")
        
        # Example 3: Handling errors
        try:
            # Intentionally calling a contract method that doesn't exist to trigger an error
            resp3 = contracts_api.call_contract_function(
                chain, contract_addr, contract_label, "thisMethodDoNotExist", post_method_args=payload
            )
            print("Example 3: Unexpectedly didn't receive an error.")
        except ApiException as e:
            # Use the SDK's ApiException which contains comprehensive error details
            error_body = getattr(e, 'body', 'No body available')
            print(f"Example 3: The callContractFunction method correctly threw an error: {e.reason} {error_body}")
        except Exception as e:
            # Fallback for any other exceptions
            print(f"Example 3: The callContractFunction method correctly threw an error: {str(e)}")
    
    except Exception as e:
        print(f"Something went wrong and examples did not complete: {str(e)}")


if __name__ == "__main__":
    main()
