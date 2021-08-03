# BlockTracker
Un outil pour remonter l'historique des transactions d'une adresse sur la Blockchain.

## Qu'est-ce que BlockTracker ?

BlockTracker est un outil permettant de suivre les transactions de plusieurs adresses de portefeuilles sur la Blockchain. Il est capable de les lister et d'établir un arbre des transactions.

Même après un mixage des fonds provenant d'un ou de plusieurs portefeuilles, il est capable de retracer les transactions jusqu'à l'adresse finale du portefeuille.

### Comment cela fonctionne-t-il ?

Développé en langage Python, l'outil utilise la bibliothèque argparse pour gérer les commandes en ligne de commande. Il utilise la bibliothèque requests pour récupérer les données de plusieurs API via une méthode GET et les trier.

Pour retracer un mélange de fonds, l'outil constitue un arbre de transactions et analyse également les adresses des destinataires. Une fois l'arbre des transactions établi, il détermine avec des probabilités la ou les adresses finales possibles.

------

## Installation

#Clonez le dépôt github

```shell
$ git clone https://github.com/thisiskeanyvy/blocktracker.git
```

#Allez dans le dossier de l'outil

```shell
$ cd blocktracker/
```

#Installation des bibliothèques Python pré-requises

```shell
$ pip3 install -r requirements.txt
```

#Exécuter l'outil avec la ligne de commande

```shell
$ python3 blocktracker.py
```

### Conditions préalables :

- Python >= 3
  - Argparse (libraries)
  - Requests (libraries)
- Pip >= 3

### Utilisation du logiciel en ligne de commande :

#Liste des commandes qui peuvent être utilisées

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

#Connaître le type de crypto-monnaie du portefeuille

```shell
$ python3 blocktracker.py -w TScgcMteFMiYzXMgWPoKkaTNnKaLWZnnPb #--whataddress
```

```shell
TRON (TRX)
```

#Obtenez l'arbre des transactions d'une ou de plusieurs adresses d'un portefeuille.

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

#### Utilisation de l'outil avancé :

#Lister les transactions de plusieurs adresses

```shell
$ python3 blocktracker.py -t address1,address2,address3 #--track
```

------

## Processus de développement

BlockTracker est publié sous les termes de la licence GPL-3.0. Voir [Licence](https://github.com/thisiskeanyvy/blocktracker/blob/main/LICENSE) pour plus d'informations ou voir https://opensource.org/licenses/GPL-3.0.

### Licence GPL-3.0 :

Les autorisations de cette licence copyleft forte sont conditionnées par la mise à disposition du code source complet des travaux sous licence et des modifications, qui incluent des travaux plus importants utilisant un travail sous licence, sous la même licence. Les avis de copyright et de licence doivent être préservés. Les contributeurs fournissent une concession expresse de droits de brevet.

### Caractéristiques :

#### Whataddress fonction :

Exécution: Hors ligne

Crypto-monnaies supportées :

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

#### Tracking fonction :

Exécution: En ligne

Type de requêtes: GET

Crypto-monnaies supportées :

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
