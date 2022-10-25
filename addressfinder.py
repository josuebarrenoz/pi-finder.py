import requests
#from pprint import pprint

def run():
    start =  int(input("Please put a initial block: "))
    end =  int(input("Please put a final block: "))
    #start =  11_000_000
    #end =  11_000_010
    l = []
    f = open ("address.txt","a")
    print(f"Started filtering through block number {start} to {end}")
    for x in range(start, end+1):
        url = requests.get("http://18.224.139.145:3001/api/explorer/block/"+str(x)).json()["data"]["txs"]
        for i in url:
            g = i["from"]
            t = i["to"]
            g1 = g not in l
            t1 = t not in l
            #print(f"Ox{g} 0x{t}")
            if g1 == True:
                l.append(g)
            if t1 in l == True:
                l.append(t)

    for i in  l:
        b = float(requests.get("http://18.224.139.145:3001/api/explorer/account/"+i+"/balance").json()["data"]["balance"])/1000000000000000000
        print(f"0x{i} {b} pi", file = f)
    f.close()


if __name__ == "__main__":
    run()

