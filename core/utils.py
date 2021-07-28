import requests, json
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def scan_transactions(track_address):
    for i in range(len(track_address)):
        try:
            sleep(1)
            data = requests.get(f'https://api.etherscan.io/api?module=account&action=txlist&address={track_address[i]}&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken').text
            data = json.loads(data)
            print(f"\nAddress n°{i+1} : {track_address[i]}")
            print("-----------------")
            print("- Transactions List -\n")
            for j in range(len(data["result"])):
                from_addr = data["result"][i]["from"]
                to_addr = data["result"][i]["to"]
                ts_addr = data["result"][i]["timeStamp"]
                print(f"Time : {ts_addr}")
                print(f"From : {from_addr}")
                print(f"To : {from_addr}")
                print("-----------------")
            print("\n")
            sleep(2)
        except:
            print("Please enter an ethereum address...")
