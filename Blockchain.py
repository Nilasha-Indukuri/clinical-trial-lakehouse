from web3 import Web3

# Connect to Ganache (default RPC port)
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Test connection
if w3.is_connected():
    print("✅ Connected to Ganache blockchain")
    print("First account:", w3.eth.accounts[0])
else:
    print("❌ Failed to connect to Ganache")
