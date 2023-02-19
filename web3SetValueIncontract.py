import json
from web3 import Web3

# Fill in your infura API key here
infura_url = "https://goerli.infura.io/v3/b3efb9a6d51945f08d54de289a845830"
account_1 = '0x0BD2c4B74c3DEcF804567eb91DF84F3fAcC6DE32'

w3 = Web3(Web3.HTTPProvider(infura_url))

# OMG Address

abi = '''[{
		"inputs": [],
		"name": "retrieve",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "num",
				"type": "uint256"
			}
		],
		"name": "store",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]'''

address = '0xA515e77Db1A9EA8135E5Ca7091ee62050781DdFB'
contract = w3.eth.contract(address=address, abi=abi)

nonce = w3.eth.getTransactionCount(account_1)

transaction = contract.functions.store(123).buildTransaction( { 'gas': 6000000,'gasPrice': w3.eth.gas_price, 'from': account_1,'nonce': nonce } )

private_key = "PRIVATE KEY"

signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key)

w3.eth.sendRawTransaction(signed_txn.rawTransaction)
