import requests, json, os
from time import sleep
from datetime import datetime
from core.graph import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def scan_transactions(track_address):
    for i in range(len(track_address)):
        if "0x" in track_address[i][0:2]:
            try:
                sleep(1)
                data = requests.get(f'https://api.etherscan.io/api?module=account&action=txlist&address={track_address[i]}&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken').text
                data = json.loads(data)
                print(f"\nAddress n°{i+1} : {track_address[i]}")
                print("-----------------")
                print("- Transactions List -\n")
                #define array variables
                columns = ["Time","From","To"]
                from_addr_array = []
                to_addr_array = []
                ts_addr_array = []
                for j in range(len(data["result"])):
                    from_addr = data["result"][j]["from"]
                    to_addr = data["result"][j]["to"]
                    ts_addr = data["result"][j]["timeStamp"]
                    ts_addr = datetime.fromtimestamp(int(ts_addr))
                    #create array
                    from_addr_array.append(from_addr)
                    to_addr_array.append(to_addr)
                    ts_addr_array.append(ts_addr)
                    #print results
                    print(f"Time : {ts_addr}")
                    print(f"From : {from_addr}")
                    if to_addr != "":
                        print(f"To : {to_addr}")
                    else:
                        print("To : Contract Creation")
                    print("-----------------")
                print("\n")
                if not os.path.exists('data'):
                    os.makedirs('data')
                full_path = os.path.join(f"{os.getcwd()}/data",f"{track_address[i]}.csv")
                file = open(full_path,"w")
                for k in range(len(from_addr_array)):
                    if to_addr_array[k] != "":
                        file.write(f"{ts_addr_array[k]},{from_addr_array[k]},{to_addr_array[k]}\n")
                    else:
                        file.write(f"{ts_addr_array[k]},{from_addr_array[k]},Contract Creation\n")
                file.close()
                if len(track_address) == 1:
                    print("Starting the graphical interface...")
                    graph(columns,track_address[i])
                sleep(2)
            except:
                print("An error has occurred please try again...")
        else:
            print("Please enter an ethereum address...")
