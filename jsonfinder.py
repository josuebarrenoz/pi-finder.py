import json


def run():
    g = open ("address.txt","a")
    with open("pichainspec.json", "r") as f:
        data = json.load(f)
        for key,value in data["accounts"].items():
            print(f"{key}",file=g)
    g.close()
    
    
if __name__ == "__main__":
    run()
