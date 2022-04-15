from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import make_response
import requests
import pprint

# fetch the company data
URL = 'http://127.0.0.1:2224/api'
comp = requests.get(URL).json()

pprint.pprint(comp)
