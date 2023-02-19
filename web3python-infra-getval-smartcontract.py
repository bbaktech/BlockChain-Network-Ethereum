import json
from web3 import Web3

# Fill in your infura API key here
infura_url = "https://goerli.infura.io/v3/b3efb9a6d51945f08d54de289a845830"

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

#abi = json.loads
# OMG ABI


address = '0xA515e77Db1A9EA8135E5Ca7091ee62050781DdFB'

contract = w3.eth.contract(address=address, abi=abi)

#totalSupply = contract.functions.retrieve().call()

#print(w3.fromWei(totalSupply, 'ether'))

print(contract.address)
#print(contract.functions.symbol().call())

balance = contract.functions.retrieve().call()

print(w3.fromWei(balance, 'ether'))
