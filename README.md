# BlockTracker
A tool to go up the transaction tree of an address on the Blockchain.

## What is BlockTracker?

BlockTracker is a tool for tracking transactions from wallet addresses on the Blockchain. It is able to list them and establish a transaction tree.

Even after mixing funds from one or more wallets, it is able to trace the transactions back to the final wallet address.

### How does it work?

Developed in the Python language, the tool uses the argparse library to handle command line commands. It uses the requests library to retrieve data from multiple API's via a GET method and then sorts it.

To trace a fund mix, the tool builds a transaction tree and also analyses the addresses of the recipients. Once the transaction tree is established, it determines with probabilities the possible final address(es).

------

## Installation

#Clone the github repository

```shell
$ git clone https://github.com/thisiskeanyvy/blocktracker.git
```

#Go to the tool's folder

```shell
$ cd blocktracker/
```

#Installing the pre-required Python libraries

```shell
$ pip3 install -r requirements.txt
```

#Run the tool with the command line

```shell
$ python3 blocktracker.py
```

### Prerequisites :

- Python >= 3
  - Argparse (libraries)
  - Requests (libraries)
- Pip >= 3

### Using the command line software :

#List the commands that can be used

```shell
$ python3 blocktracker.py -h #--help
```

```shell
usage: blocktracker.py [-h] [-w WHATADDRESS] [-t TRACK]

optional arguments:
-h, --help       show this help message and exit
-w WHATADDRESS, --whataddress WHATADDRESS
Get type of wallet address
-t TRACK, --track TRACK
Get all transactions from an address
```

#Know the type of crypto-currency in the wallet

```shell
$ python3 blocktracker.py -w TScgcMteFMiYzXMgWPoKkaTNnKaLWZnnPb #--whataddress
```

```shell
TRON (TRX)
```

#Get the transaction tree of one or more addresses of a wallet

```shell
$ python3 blocktracker.py -t 0xbaf681271070c832DbB217665ACf0005f0A87A0c #--track
```

```shell
Address n°1 : 0xbaf681271070c832DbB217665ACf0005f0A87A0c
-----------------
- Transactions List -

Time : 2019-03-24 20:46:47
From : 0x6a67e74a202949c6a08496cd764452970135862c
To : 0x6a67e74a202949c6a08496cd764452970135862c
-----------------
Time : 2019-03-24 20:54:24
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-03-25 18:19:42
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-03-25 18:29:21
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-03-25 18:33:11
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-03-27 21:27:38
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-03-27 21:42:05
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-03-27 23:02:56
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-07-07 22:57:04
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-07-07 23:35:16
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-07-11 01:11:11
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-07-15 00:51:09
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-09-06 23:36:25
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
Time : 2019-12-26 17:08:43
From : 0xbaf681271070c832dbb217665acf0005f0a87a0c
To : 0xbaf681271070c832dbb217665acf0005f0a87a0c
-----------------
```

#### Using the advanced tool :

#List the transactions of several addresses

```shell
$ python3 blocktracker.py -t address1,address2,address3 #--track
```

------

## Development Process

BlockTracker is released under the terms of the GPL-3.0 license. See [Licence](https://github.com/thisiskeanyvy/blocktracker/blob/main/LICENSE) for more information or see https://opensource.org/licenses/GPL-3.0.

### Licence GPL-3.0 :

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

### Features :

#### Whataddress function :

Execution: Offline

Supported crypto-currencies :

- [x] Ethereum (ETH)
- [x] Bitcoin (BTC)
- [x] Bitcoin Cash (BCH)
- [x] Cardano (ADA)
- [x] Cosmos (ATOM)
- [x] Dash (DASH)
- [x] Dogecoin (DOGE)
- [x] Komodo (KMD)
- [x] Lisk (LSK)
- [x] Litecoin (LTC)
- [x] NEM (XEM)
- [x] NEO (NEO)
- [x] Ontology (ONT)
- [x] Polkadot (DOT)
- [x] Ripple (XRP)
- [x] Stellar (XLM)
- [x] Tezos (XTZ)
- [x] TRON (TRX)
- [x] Waves (WAVES)
- [x] Zcash (ZEC)

#### Tracking function :

Execution: Online

Type of requests: GET

Supported crypto-currencies :

- [x] Ethereum (ETH)
- [ ] Bitcoin (BTC)
- [ ] Bitcoin Cash (BCH)
- [ ] Cardano (ADA)
- [ ] Cosmos (ATOM)
- [ ] Dash (DASH)
- [ ] Dogecoin (DOGE)
- [ ] Komodo (KMD)
- [ ] Lisk (LSK)
- [ ] Litecoin (LTC)
- [ ] NEM (XEM)
- [ ] NEO (NEO)
- [ ] Ontology (ONT)
- [ ] Polkadot (DOT)
- [ ] Ripple (XRP)
- [ ] Stellar (XLM)
- [ ] Tezos (XTZ)
- [ ] TRON (TRX)
- [ ] Waves (WAVES)
- [ ] Zcash (ZEC)

------
