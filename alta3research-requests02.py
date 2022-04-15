from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import make_response
import requests
import pprint

# fetch the company data and return readable text
URL = 'http://127.0.0.1:2224/api'
comp = requests.get(URL).json()
print('Company Data:')
print('Company Name:', end='')
pprint.pprint(comp[0]['company'])
print('Ticker:', end='')
pprint.pprint(comp[0]['stockTicker'])
print('CEO:', end='')
pprint.pprint(comp[0]['CEO'])
print('Departments:', end='')
pprint.pprint(comp[0]['departments'])
print('Positions:', end='')
pprint.pprint(comp[0]['positions'])


print("-----------------------------------------------")


# fetch inventory data and return readable text
URL2 = 'http://127.0.0.1:2224/api/inventory'
items = requests.get(URL2).json()
print("Items for sale:")
print('Phones:', end='')
pprint.pprint(items[0]['phones'])
print('Computers:', end='')
pprint.pprint(items[0]['computers'])
print('Gaming:', end='')
pprint.pprint(items[0]['phones'])
print('Cars:', end='')
pprint.pprint(items[0]['cars'])
print('Robots:', end='')
pprint.pprint(items[0]['robots'])
print('Other:', end='')
pprint.pprint(items[0]['other'])
print('Inventory Count:', end='')
pprint.pprint(items[0]['inventoryCount'])
