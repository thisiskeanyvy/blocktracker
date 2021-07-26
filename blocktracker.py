import os, argparse
from time import sleep

#init
parse = argparse.ArgumentParser()
parse.add_argument('-w', '--whataddress', help='Get type of wallet address', dest='whataddress')
args = parse.parse_args()

#variables
unk_address = args.whataddress.split(',')

"""
Address format (start with):
0x - Ethereum (ETH)
3 - Bitcoin (BTC)
bitcoincash:q - Bitcoin Cash (BCH)
addr - Cardano (ADA)
cosmos - Cosmos (ATOM)
X - Dash (DASH)
D - Dogecoin (DOGE)
R - Komodo (KMD)
L - Lisk (LSK)
M - Litecoin (LTC)
N - NEM (XEM)
A - NEO (NEO)
A - Ontology (ONT)
1 - Polkadot (DOT)
r - Ripple (XRP)
G - Stellar (XLM)
tz - Tezos (XTZ)
T - TRON (TRX)
3P - Waves (WAVES)
t1 or t2 - Zcash (ZEC)
"""

def whataddress(): #try to determine type of wallet address
    for i in range(len(unk_address)): #offline verification
        address_toverify = unk_address[i];
        if "0x" in address_toverify[0:2]:
            print("Ethereum (ETH)")
        elif "tz" in address_toverify[0:2]:
            print("Tezos (XTZ)")
        elif "3P" in address_toverify[0:2]:
            print("Waves (WAVES)")
        elif "t1" in address_toverify[0:2] or "t2" in address_toverify[0:2]:
            print("Zcash (ZEC)")
        elif "bitcoincash:q" in address_toverify[0:13]:
            print("Bitcoin Cash (BCH)")
        elif "addr" in address_toverify[0:4]:
            print("Cardano (ADA)")
        elif "cosmos" in address_toverify[0:5]:
            print("Cosmos (ATOM)")
        elif "3" in address_toverify[0:1]:
            print("Bitcoin (BTC)")
        elif "X" in address_toverify[0:1]:
            print("Dash (DASH)")
        elif "D" in address_toverify[0:1]:
            print("Dogecoin (DOGE)")
        elif "R" in address_toverify[0:1]:
            print("Komodo (KMD)")
        elif "L" in address_toverify[0:1]:
            print("Lisk (LSK)")
        elif "M" in address_toverify[0:1]:
            print("Litecoin (LTC)")
        elif "N" in address_toverify[0:1]:
            print("NEM (XEM)")
        elif "A" in address_toverify[0:1]:
            print("NEO (NEO) or Ontology (ONT)")
        elif "1" in address_toverify[0:1]:
            print("Polkadot (DOT)")
        elif "r" in address_toverify[0:1]:
            print("Ripple (XRP)")
        elif "G" in address_toverify[0:1]:
            print("Stellar (XLM)")
        elif "T" in address_toverify[0:1]:
            print("TRON (TRX)")
        else:
            print("Addtess type unknown or not supported ???")

if __name__ == "__main__":
    whataddress()
