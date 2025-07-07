# MultiBaas Python SDK Examples

This directory contains examples demonstrating how to use the MultiBaas Python SDK.

## Setup

1. Create a virtual environments with the tool of your choice (here we use venv):

```bash
python -m venv venv
source venv/bin/activate
```

2. Install the SDK and required dependencies:
```bash
# For development/testing with the local SDK
pip install -e ../
pip install -r requirements.txt
```

Or for testing with a built package:
```bash
# Build the SDK package first
cd ..
python -m build

# Install the built wheel
pip install ../dist/multibaas_sdk-*.whl
pip install -r requirements.txt
```

2. Create a `.env` file in this directory with your MultiBaas credentials:
```
MB_BASE_URL=https://your-multibaas-instance.example.com
MB_API_KEY=your_api_key_here
```

## Running the Examples

### Basic Usage Example

The `main.py` script demonstrates basic usage of the MultiBaas Python SDK, including:

1. Getting blockchain details (chain ID and latest block number)
2. Calling a smart contract function (ERC20 balanceOf)
3. Handling errors properly

To run the example:

```bash
python main.py
```

## Sample Output

When run successfully, the example script will output information similar to:

```
Example 1: MultiBaas is connected to the chain ID #11155111 and the latest block number is #12345678
Example 2: The wallet 0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B balance on the ERC20 contract 0x969D499507B4f437953Db24A4980FdEEDa6Db8a1 is: 0.000000000000000000
Example 3: The callContractFunction method correctly threw an error: Bad Request {"status":400,"message":"Method not found"}
```