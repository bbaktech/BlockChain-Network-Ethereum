from web3 import Web3

infura_url = "https://goerli.infura.io/v3/b3efb9a6d51945f08d54de289a845830"
web3 = Web3(Web3.HTTPProvider(infura_url))
#account_1 = '0x0BD2c4B74c3DEcF804567eb91DF84F3fAcC6DE32'


tx = web3.eth.get_transaction('0x5a3dd2c0e022da79330d19835f6abb5341a78a84e7a1f73f64c1c4e09ed5a07b')

print(tx)

