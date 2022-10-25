import requests


def searchaccount(account):
    url = requests.get("http://18.224.139.145:3001/api/explorer/account/"+account+"/txs").json()["data"]
    c = 0
    for i in url:
        f = i["from"]
        t = i["to"]
        v = float(i["value"])/1000000000000000000
		# h = i["txHash"]
		# b = i["includedInBlock"]
        c = c+1
    	# print(f"Transaccion N°{c} from {f} to {t} value {v} pi by hash {h} in block {b}")
        print(f"Transaccion N°{c} from Ox{f} to Ox{t} value {v} pi")


def run():
    account =  str((input("Please put a valid address: ")))
    searchaccount(account)


if __name__ == "__main__":
    run()

