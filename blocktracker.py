import os, argparse
from time import sleep
from core.colors import *
from core.utils import *

#init
parse = argparse.ArgumentParser()
parse.add_argument('-w', '--whataddress', help='Get type of wallet address', dest='whataddress')
parse.add_argument('-t', '--track', help='Get all transactions from an address', dest='track')
args = parse.parse_args()

#just the banner of the software
def banner():
    print(yellow + "                                                        ,----,")
    print("                                                      ,/   .`|")
    print("    ,---,.   ,--,                            ,-.    ,`   .'  :                                 ,-.")
    print("  ,'  .'  \,--.'|                        ,--/ /|  ;    ;     /                             ,--/ /|")
    print(",---.' .' ||  | :     ,---.            ,--. :/ |.'___,/    ,' __  ,-.                    ,--. :/ |             __  ,-.")
    print("|   |  |: |:  : '    '   ,'\           :  : ' / |    :     |,' ,'/ /|                    :  : ' /            ,' ,'/ /|")
    print(":   :  :  /|  ' |   /   /   |   ,---.  |  '  /  ;    |.';  ;'  | |' | ,--.--.     ,---.  |  '  /      ,---.  '  | |' |")
    print(":   |    ; '  | |  .   ; ,. :  /     \ '  |  :  `----'  |  ||  |   ,'/       \   /     \ '  |  :     /     \ |  |   ,'")
    print("|   :     \|  | :  '   | |: : /    / ' |  |   \     '   :  ;'  :  / .--.  .-. | /    / ' |  |   \   /    /  |'  :  /")
    print("|   |   . |'  : |__'   | .; :.    ' /  '  : |. \    |   |  '|  | '   \__\/: . ..    ' /  '  : |. \ .    ' / ||  | '")
    print("'   :  '; ||  | '.'|   :    |'   ; :__ |  | ' \ \   '   :  |;  : |   ,' .--.; |'   ; :__ |  | ' \ \'   ;   /|;  : |")
    print("|   |  | ; ;  :    ;\   \  / '   | '.'|'  : |--'    ;   |.' |  , ;  /  /  ,.  |'   | '.'|'  : |--' '   |  / ||  , ;")
    print("|   :   /  |  ,   /  `----'  |   :    :;  |,'       '---'    ---'  ;  :   .'   \   :    :;  |,'    |   :    | ---'")
    print("|   | ,'    ---`-'            \   \  / '--'                        |  ,     .-./\   \  / '--'       \   \  /")
    print("`----'                         `----'                               `--`---'     `----'              `----'\n")
    message()

def message():
    print(f"""{red}   Search and track blockchain transactions from a wallet address       {green}°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸{red}
    ~ Code by Keany Vy KHUN \ Python program \ {sys.platform}             {white}°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸{red}
     - Github : https://github.com/thisiskeanyvy        {green}°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸{red}
      # Instagram : https://instagram.com/thisiskeanyvy         {white}°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸{red}
       ^ Twitter : https://twitter.com/thisiskeanyvy                       {green}°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸{red}
    """)

def help():
    print(f"""
     -------------------------------------------------------------          {white}H{red}e{white}l{red}l{white}o{red} {white}W{red}o{white}r{red}l{white}d {red}!
    |  usage: blocktracker.py [-h] [-w WHATADDRESS] [-t TRACK]    |               {white}__...--~~~~~-._   _.-~~~~~--...__{red}
    |                                                             |             {white}//               `V'               \\{red}
    |  optional arguments:                                        |            {white}//                 |                 \\{red}
    |  -h, --help            show this help message and exit      |           {white}//__...--~~~~~~-._  |  _.-~~~~~~--...__\\{red}
    |  -w WHATADDRESS, --whataddress WHATADDRESS                  |          {white}//__.....----~~~~._\ | /_.~~~~----.....__\\{red}
    |  Get type of wallet address                                 |         {white}====================\\|//===================={red}
    |  -t TRACK, --track TRACK                                    |                         {green}BlockTracker `---`{red}
    |  Get all transactions from an address                       |
     -------------------------------------------------------------""")

#variables
try:
    unk_address = args.whataddress.split(',')
except:
    try:
        track_address = args.track.split(',')
    except:
        banner()

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
        if '0x' in address_toverify[0:2]:
            print("Ethereum (ETH)")
        elif 'tz' in address_toverify[0:2]:
            print("Tezos (XTZ)")
        elif '3P' in address_toverify[0:2]:
            print("Waves (WAVES)")
        elif 't1' in address_toverify[0:2] or 't2' in address_toverify[0:2]:
            print("Zcash (ZEC)")
        elif 'bitcoincash:q' in address_toverify[0:13]:
            print("Bitcoin Cash (BCH)")
        elif 'addr' in address_toverify[0:4]:
            print("Cardano (ADA)")
        elif 'cosmos' in address_toverify[0:5]:
            print("Cosmos (ATOM)")
        elif '3' in address_toverify[0:1]:
            print("Bitcoin (BTC)")
        elif 'X' in address_toverify[0:1]:
            print("Dash (DASH)")
        elif 'D' in address_toverify[0:1]:
            print("Dogecoin (DOGE)")
        elif 'R' in address_toverify[0:1]:
            print("Komodo (KMD)")
        elif 'L' in address_toverify[0:1]:
            print("Lisk (LSK)")
        elif 'M' in address_toverify[0:1]:
            print("Litecoin (LTC)")
        elif 'N' in address_toverify[0:1]:
            print("NEM (XEM)")
        elif 'A' in address_toverify[0:1]:
            print("NEO (NEO) or Ontology (ONT)")
        elif '1' in address_toverify[0:1]:
            print("Polkadot (DOT)")
        elif 'r' in address_toverify[0:1]:
            print("Ripple (XRP)")
        elif 'G' in address_toverify[0:1]:
            print("Stellar (XLM)")
        elif 'T' in address_toverify[0:1]:
            print("TRON (TRX)")
        else:
            print("Addtess type unknown or not supported ???")

#start function
try:
    if unk_address:
        whataddress()
except:
    try:
        if track_address:
            scan_transactions(track_address)
    except:
        help()
