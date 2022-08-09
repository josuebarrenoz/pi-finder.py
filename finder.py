#import dependencies
#import pickle
#import sys
from web3 import Web3, HTTPProvider

#instantiate a web3 remote provider
w3 = Web3(HTTPProvider('http://3.128.144.155:23001'))

#request the latest block number
ending_blocknumber1 = w3.eth.blockNumber
ending_blocknumber = 12900673

#latest block number minus 100 blocks
starting_blocknumber = 12620050

#filter through blocks and look for transactions involving this address
#blockchain_address = "0x5d9d830d89e260e733f073c4d80ff58caf3ac6bb"

#create an empty dictionary we will add transaction data to
#tx_dictionary = {}

def getTransactions(start, end):
    '''This function takes three inputs, a starting block number, ending block number
    and an Ethereum address. The function loops over the transactions in each block and
    checks if the address in the to field matches the one we set in the blockchain_address.
    Additionally, it will write the found transactions to a pickle file for quickly serializing and de-serializing
    a Python object.'''

    print(f"Started filtering through block number {start} to {end}")
    for x in range(start, end):
        print(f"Checking block number {x}")
        block = w3.eth.getBlock(x, True)
        for transaction in block.transactions:
            a = str(transaction["from"])
            b = str(transaction["to"])
            #h = transaction["hash"]
            #c = str(address)

            
            print(f"{x} {a} {b}",file = f)

            # if transaction['to'] == address or transaction['from'] == address:
            #     with open("transactions.pkl", "wb") as f:
            #         hashStr = transaction['hash'].hex()
            #         tx_dictionary[hashStr] = transaction
            #         pickle.dump(tx_dictionary, f)
            #     f.close()
    #print(f"Finished searching blocks {start} through {end} and found {len(tx_dictionary)} transactions")

f = open ("output.txt","a")
getTransactions(starting_blocknumber, ending_blocknumber)
f.close()
