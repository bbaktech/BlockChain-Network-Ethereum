from web3 import Web3

infura_url = "https://goerli.infura.io/v3/b3efb9a6d51945f08d54de289a845830"
web3 = Web3(Web3.HTTPProvider(infura_url))
account_1 = '0x0BD2c4B74c3DEcF804567eb91DF84F3fAcC6DE32'
private_key1 = 'Private Key'
account_2 = '0xD1ED7acB72F84134203BB25AA0F5395a876BE18c'

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'gwei'),
    'gas': 6000000,
    'gasPrice': web3.eth.gas_price
}
#  optional field 'gasPrice': web3.eth.gas_price in tx
print(tx)
print('----------------------------------------')
#gas = web3.eth.estimate_gas(tx)
#tx.update({'gas': gas})

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key1)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print(web3.toHex(tx_hash))

tx = web3.eth.get_transaction(tx_hash)

print(tx)
