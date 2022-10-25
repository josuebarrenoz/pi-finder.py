import requests
import datetime

l = []
f = open ("output.txt","a")

def wallet_finder(start, end):
    initial_time = datetime.datetime.now()
    print(f"Started filtering through block number {start} to {end} at {datetime.datetime.now()}...")

    for x in range(start, end+1):
        #print(f"Searching block number {x}")
        url1 = requests.get("http://localhost:3001/api/explorer/block/"+str(x)).json()["data"]["txs"]
        for i in url1:
            print(f"Searching block number {x}")
            if i["from"] == "0xb76350e79beacade46a2b1ad06a1e6b31236407f" or i["to"] == "0xb76350e79beacade46a2b1ad06a1e6b31236407f" :
                print(f"wallet located in block {x}:", file = f)
                print(f"wallet located in block {x}:")

def run():
    start =  int(input("Please put the initial block: "))
    end =  int(input("Please put the final block: "))
    wallet_finder(start, end)


if __name__ == "__main__":
    run()
