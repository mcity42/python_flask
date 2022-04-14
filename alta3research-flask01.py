#!/usr/bin/env python3
"""Flask Application"""

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import make_response
import requests

app = Flask(__name__)

herodata = [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
    ]
}]

# endpoint that returns plain json


# render html to endpoint
@app.route('/')
def index():
    return render_template('login.html')


# render json to endpoint
@app.route("/api")
def son():
    # jsonify returns legal JSON
    return jsonify(herodata)

# set the cookie and send it back to the user


@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    # if user generates a POST to our API
    if request.method == "POST":
        # if nm was assigned via the POST
        if request.form.get("nm") and request.form.get('pos'):
            # if request.form["nm"] <-- this also works, but returns ERROR if no nm
            user = request.form.get("nm")  # grab the value of nm from the POST
            pos = request.form.get("pos")
            # team = request.form.get("tm")
            # teammates = request.form.get("tms")
        else:  # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"
            pos = 'default'
            # team = 'default'
            # teammates = 'default'

        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
        # cookievar #value
        resp.set_cookie("userID", user)
        resp.set_cookie("position", pos)
        # resp.set_cookie("team", team)
        # resp.set_cookie("teammates", teammates)

        # return our response object includes our cookie
        return resp

    if request.method == "GET":  # if the user sends a GET
        return redirect(url_for("index"))  # redirect to index

# check users cookie for their name


@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID")  # preferred method
    role = request.cookies.get("position").strip()
    # squad = request.cookies.get("team")
    # members = request.cookies.get("teammates")
    # name = request.cookies["userID"] # <-- this works but returns error
    # if value userID is not in cookie

    player = {
        'name': name,
        'position': role,
        # 'team': squad,
        # 'teammates': [members]
    }
    #reso = requests.get("")

    # return HTML embedded with name (value of userID read from cookie)
    return f'<h1>Welcome {player}</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
