#import dependencies
#import pickle
#import sys
from web3 import Web3, HTTPProvider

#instantiate a web3 remote provider
w3 = Web3(HTTPProvider('http://3.128.144.155:23001'))

# request the latest block number
# how request the last block number => ending_blocknumber = w3.eth.blockNumber
# ending_blocknumber = 12900673

#latest block number minus 100 blocks
#starting_blocknumber = 12646797

#filter through blocks and look for transactions involving this address
#blockchain_address = "0x5d9d830d89e260e733f073c4d80ff58caf3ac6bb"

#create an empty dictionary we will add transaction data to
#tx_dictionary = {}


def getTransactions(start, end, address):
    '''This function takes three inputs, a starting block number, ending block number
    and an Ethereum address. The function loops over the transactions in each block and
    checks if the address in the to field matches the one we set in the blockchain_address.
    Additionally, it will write the found transactions to a pickle file for quickly serializing and de-serializing
    a Python object.'''

    print(f"Started filtering through block number {start} to {end}")
    for x in range(start, end+1):
        print(f"Checking block number {x}")
        block = w3.eth.getBlock(x, True)
        for transaction in block.transactions:
            a = str(transaction["from"])
            #al = a.lower()
            b = str(transaction["to"])
            #bl = b.lower()
            #h = transaction["hash"]
            #c = str(address)
            if a.lower() == address or b.lower() == address:
                print(f"{x} {a} {b}",file = f)
                print(f"MATCH! IN BLOCK {x}!!!")
            # if transaction['to'] == address or transaction['from'] == address:
            #     with open("transactions.pkl", "wb") as f:
            #         hashStr = transaction['hash'].hex()
            #         tx_dictionary[hashStr] = transaction
            #         pickle.dump(tx_dictionary, f)
            #     f.close()
    
    	# print(f"Finished searching blocks {start} through {end}")

	# f = open ("output.txt","a")
	# getTransactions(starting_blocknumber, ending_blocknumber, blockchain_address)
	# f.close()


if __name__ == "__main__":
    print(f"Inicializing finder_filter.py ......")
    starting_blocknumber = int(input("Find transactions from block number: "))
    ending_blocknumber = int(input("Until block number: "))
    blockchain_address = str(input("Put a blockchain address to find: "))
    f = open ("output_filter.txt","a")
    # getTransactions(starting_blocknumber, ending_blocknumber, blockchain_address)
    getTransactions(starting_blocknumber, ending_blocknumber, blockchain_address)
    f.close()
