# Status

[![Build Status](https://travis-ci.org/arxanchain/tomago-sdk-py.svg?branch=master)](https://travis-ci.org/arxanchain/tomago-sdk-py)

# tomago-sdk-py

Tomago is a project code name, which is used to wrap SmartContract invocation
from the business point of view, including APIs for managing digital assets,
asset owners (entities), etc. management, digital assets, etc. You need not
care about how the backend blockchain runs or the unintelligible techniques,
such as consensus, endorsement and decentralization. Simply use the SDK we
provide to implement your business logics, we will handle the caching, tagging,
compressing, encrypting and high availability.

We also provide a way from this SDK to invoke the SmartContract, a.k.a.
Chaincode, which is deployed by yourself.

This SDK enables *Python* developers to develop applications that interact with the
SmartContract which is deployed out of the box or by yourself in the ArxanChain
BaaS Platform via Tomago.

# Usage

## Install

Run following command to download the Python SDK

```code
$ git clone -b v2.0.1 https://github.com/arxanchain/tomago-sdk-py.git
$ cd tomago-sdk-py
$ python setup.py install
```

## Request APIKey and download certificates

Before using the Tomago SDK Client, you need to request an APIKey and download
the certificates from ArxanChain BaaS ChainConsole for data encryption and
signing. This will help ensure the data cannot be tampered with or illegally
accessed to even if the client communicates with Tomago service via HTTPS.

The certificates include:

* The public key of ArxanChain BaaS Platform (server.crt) which is used to
  encrypt the data sent to Tomago service. You can download it from the
  ArxanChain BaaS ChainConsole -> System Management -> API Certs Management
* The private key of the client user (such as `APIKey.key`) which is used to sign the
  data. You can download it when you create an API Certificate.

After downloading the two certificates, you need to configure your installed
py-common package.
For more details please refer to [the usage of py-common](https://github.com/arxanchain/py-common#usage)

### Init a Client
A Client object is used to wrap all the encryption/decryption details, any API call
to the BaaS service needs to use this object., you can register a client object as follows:

```python
>>> from rest.api.api import Client
>>> apikey = "pWEzB4yMM1518346407"
>>> cert_path = "/usr/local/lib/python2.7/site-packages/py_common-2.0.1-py2.7.egg/cryption/ecc/certs"
>>> ent_sign_param = {}
>>> ip_addr = "http://127.0.0.1:9143"
>>> client = Client(apikey, cert_path, ent_sign_param, ip_addr)
```

* **apikey** is used to set the API access key applied on `ChainConsole` management page,
* **cert_path** is the path of your private key file and tls certificate,
* **ip_addr** is the IP address of the BAAS server entrance(*wasabi* or *wallet* service). 
* **ent_sign_param** is the enterprise sign params dictionary, but it's unnecessary for tomago, so it can be empty

If you want to bypass the wasabi service, you need to add param enable_crypto=False.

### Register a blockchain Client

To invoke the SDK API, you first have to create a blockchain client as follows:

```python
>>> from tomago.api.blockchain import BlockChain
>>> bc = BlockChain(client)
```

When building the blockchain client configuration, **client** fields must
be set.

* Invoke a chaincode function

After creating the blockchain client, you can use it to invoke a blockchain
as follows:

```python
>>> header = {
...     "Channel-Id": "pubchain"
...     }
>>> body = {
...     "payload":  {
...         "chaincode_id": "pubchain-mycc",
...         "args": ["invoke", "a", "b", "1"],
...     }
... }
>>> _, resp = bc.invoke(header, body)
>>> print resp
```

  - Channel-Id: This is your private blockchain ID, you can get this ID from
    the System Admin. If the chaincode is published on the public blockchain,
    you need not set this in http header.
  - chaincode_id: The name of the chaincode when you publish it into the
    production blockchain environment
  - args: The first element of this array is the function name that you want to
    invoke, the rest are the arguments of the function

* Query a chaincode function

```python
>>> header = {
...     "Channel-Id": "pubchain"
...     }
>>> body = {
...     "payload":  {
...         "chaincode_id": "pubchain-mycc",
...         "args": ["query", "a"],
...     }
... }
>>> _, resp = bc.query(header, body)
>>> print resp
```

* Query a chaincode transaction

```python
>>> txid = "mytxid"
>>> header = {
...     "Channel-Id": "pubchain"
...     }
>>> _, resp = bc.query_txn(header, txid)
>>> print resp
```

  - txid: The transaction id

## Issue digital assets

Deprecated, asset management related APIs have been moved into wallet-sdk-py

## Colored Coin

Deprecated, colored coin has been moved into wallet-sdk-py
