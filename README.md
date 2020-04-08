# Python Converge API

A simple, easy to use wrapper for Elavon's Converge API via key value pairs instead of XML.

## Compatibility
This package will work with python 2 and 3

## Installation

```
wget https://github.com/wontonst/python-converge-api/archive/master.zip
unzip python-converge-api-master.zip
pip install python-converge-api-master
```

## Example usage
Construct a new instance with your merchant ID, user ID, PIN and if you're using demo credentials or not.
```
c = Converge('your merchant id', 'your user id', 'your pin', is_demo=True)
```
You can then call any of the Converge transaction type with `->request()` and provide the transaction type as well as an array of key value pairs to send to the API. The package will use the demo or live endpoint automatically based on how you constructed the object.

### ccsale
```
response = c.request(
    'ccsale',
    ssl_card_number='***********7813',
    ssl_exp_date='0124',
    ssl_cvv2cvc2='1234',
    ssl_amount='10.00',
    ssl_avs_address='123 easy st',
    ssl_avs_zip='94041',
    ssl_3dsecure_value='false'
)
print(response)
{'errorCode': '5000', 'errorMessage': 'The Credit Card Number supplied in the authorization request appears to be invalid.', 'success': False, 'errorName': 'Credit Card Number Invalid'}
```
### All Transaction Types
```
* ccauthonly
* ccavsonly
* ccsale
* ccverify
* ccgettoken
* cccredit
* ccforce
* ccbalinquiry
* ccgettoken
* ccreturn
* ccvoid
* cccomplete
* ccdelete
* ccupdatetip
* ccsignature
* ccaddrecurring
* ccaddinstall
* ccupdatetoken
* ccdeletetoken
* ccquerytoken
```
