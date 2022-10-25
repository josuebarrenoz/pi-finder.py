import requests
import datetime

l = []

def charging_list():
    #open and read the file address.txt and add the wallets to the list witthout the last character    
    with open("wallets_pi2.txt", "r") as f:
        for line in f:
            l.append(line[:-1])
        f.close()

def balance():
    print(f"Searching balance for {len(l)} wallets at {datetime.datetime.now()}...")
    with open("balance2.txt", "a") as e:
        for i in  l:
            response = requests.get("http://localhost:3001/api/explorer/account/"+i+"/balance").json()["data"]["balance"]
            balance = float(response)/1000000000000000000
            print(f"{i}")
            print(f"{i} {balance}", file = e)
        e.close()
        print(f"Process ended at {datetime.datetime.now()}...")

def run():
    charging_list()
    balance()

if __name__ == "__main__":
    run()
