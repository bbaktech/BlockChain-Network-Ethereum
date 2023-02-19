
from web3 import Web3

infura_url = "https://goerli.infura.io/v3/b3efb9a6d51945f08d54de289a845830"
w3 = Web3(Web3.HTTPProvider(infura_url))

if w3.isConnected():
    print(w3.eth.blockNumber)
    # Fill in your account here
    balance = w3.eth.getBalance("0x0BD2c4B74c3DEcF804567eb91DF84F3fAcC6DE32")
    print(w3.fromWei(balance, "ether"))

