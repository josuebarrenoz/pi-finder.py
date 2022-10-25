import requests
import datetime

l = []
f = open("address.txt","a")
e = open ("errors.txt", "a")

def wallet_finder(start, end):

    initial_time = datetime.datetime.now()
    print(f"Started filtering through block number {start} to {end} at {datetime.datetime.now()}...")

    for x in range(start, end+1):
        print(f"Searching block number {x}")
        url1 = requests.get("http://localhost:3001/api/explorer/block/"+str(x)).json()["data"]["txs"]
        for i in url1:
            try:
                if i["from"] not in l:
                    l.append(i["from"])
                    print(f"{i['from']}", file=f)
                if i["to"] not in l:
                    l.append(i["to"])
                    print(f"{i['to']}", file=f)
            except TypeError:
                print(f"Block {x} not found")
                print(f"Block {x} not found", file=e)
                continue
            
    ending_time = datetime.datetime.now()
    print(f"{len(l)} wallets founded between blocks {start} and {end} in {ending_time - initial_time}:")
    #print(f"{len(l)} wallets founded between blocks {start} and {end}:", file = f)
    #print(l, file = f)

def balance():
    print(f"Searching balance for {len(l)} wallets at {datetime.datetime.now()}...")
    for i in  l:
        url2 = float(requests.get("http://localhost:3001/api/explorer/account/"+i+"/balance").json()["data"]["balance"])/1000000000000000000
        print(f"0x{i} {url2} pi", file = f)
    f.close()
    print(f"Process ended at {datetime.datetime.now()}...")

def continue_search(start, end):
    #open and read the file address.txt and add the wallets to the list witthout the last 2 characters
    with open("address.txt", "r") as f:
        for line in f:
            l.append(line[:-1])
    wallet_finder(start, end)
    

def run():
    start =  int(input("Please put the initial block: "))
    end =  int(input("Please put the final block: "))
    continue_search(start, end)
    f.close()
    e.close()
    #balance()


if __name__ == "__main__":
    run()

