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

companyData = [{
    "company": "Malik's Company",
    "stockTicker": "MC",
    "yearlyRevenue": "21.3 B",
    "since": 1996,
    "industries": [
        "engineering",
        "manufacuring",
        "supply chain",
        "eCommerce"
    ],
    "CEO": 'Malik City',
    "employeeCount": 12457,
    "departments": [
        "human resources",
        "engineering",
        "executive suite",
        "shipping",
        "customer service"
    ],
    "positions": ['Software Engineer', 'Data Scientist', 'Automation Engineer', 'Cloud Engineer',
                  'Truck Driver', 'Recruiter', 'Manager', 'Web Developer', 'Warehouse Specialist']
}]


inventoryData = [{
    "phones": ['iphone 12', 'iphone 11', 'Motorola Edge', 'Google Pixel'],
    "computers": ["MacBook Pro", "HP 255", "Lenovo Ideapad"],
    "gaming systems": ["PS5", "Xbox X", "Nintendo Wii", "PS4"],
    "Cars": 'Tesla Model 3',
    "invenoryCount": 953427,
    "robots": "Astro 3",
    "other": [
        "Apple Watch",
        "Apple Ipad",
        "Amazon Fire",
        "Amazon Firestick",
        "AppleTV"
    ]
}]


# render html to endpoint
@app.route('/')
def index():
    return render_template('login.html')


# render json to endpoint
@app.route("/api")
def compInfo():
    # jsonify returns legal JSON
    return jsonify(companyData)

# render json to endpoint


@app.route("/api/inventory")
def empInfo():
    # jsonify returns legal JSON
    return jsonify(inventoryData)


# set the cookie and send it back to the user
@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    # if user generates a POST to our API
    if request.method == "POST":
        # if nm was assigned via the POST
        if request.form.get("nm"):
            # if request.form["nm"] <-- this also works, but returns ERROR if no nm
            user = request.form.get("nm")  # grab the value of nm from the POST
            pos = request.form.get("pos")
            dob = request.form.get("tm")
            why = request.form.get("tms")
            if why == '':
                why = 'Unanswered'
        else:  # if a user sent a post without nm then assign value defaultuser
            return redirect(url_for('setcookie'))

        player = {'Name': user, 'Position': pos, 'DOB': dob, 'Response': why}
        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
        # cookievar #value
        resp.set_cookie("userID", user)
        resp.set_cookie("position", pos)
        resp.set_cookie("dob", dob)
        resp.set_cookie("reason", why)

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
    birth = request.cookies.get("dob")
    reason = request.cookies.get("reason")
    # name = request.cookies["userID"] # <-- this works but returns error
    # if value userID is not in cookie

    returnMessage = f'<h1>Congrats {name}!</h1>\n<p>You have successfully applied to our {role} role.</p>\n<p>What happens next: ' \
        'Our talented HR team will review the application and forward your contact information to a hiring team\'s manager.</p>' \
        '<p>If selected within a week, you will be scheduled in 3 rounds of coding interviews and a scavenger hunt.</p>\n<p>Good Luck</p>' \
        f'<table><thead><tr><th>Field</th><th>Input</th></tr></thead><tbody><tr><td>Name</td><td>{name}</td></tr><tr><td>Birthdate</td><td>{birth}</td>' \
        f'</tr><tr><td>Position</td><td>{role}</td></tr></tbody><tfoot><tr><td>Answer</td><td>{reason}</td></tr></tfoot></table>'

    #f'<h5>Name: {name}\nPosition: {role}\nDOB: {birth}\nAnswer: {reason}<h5>'
    # return HTML embedded with name (value of userID read from cookie)
    # return f'<h1>Congrats {name}!</h1>\n<p>You have successfully applied to our {role} role.</p>\n'
    return returnMessage


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
