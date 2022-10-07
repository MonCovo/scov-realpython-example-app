from flask import Flask
import csv
import re

app = Flask(__name__)

@app.route("/api/customer/<telno>")
def customerbynumber(telno):
    telno = re.sub('[^0-9]','', telno)
    reader = csv.DictReader(open('data/caller_info.csv', 'r'), delimiter = ',', quotechar="\"")
    for rec in reader:
        value = rec['number']
        if str(value) == str(telno):
            return rec
    return ('', 204)

@app.route("/api/car/<telno>")
def carbynumber(telno):
    telno = re.sub('[^0-9]','', telno)
    reader = csv.DictReader(open('data/car_numbers.csv', 'r'), delimiter = ',', quotechar="\"")
    for rec in reader:
        value = rec['number']
        if str(value) == str(telno):
            return rec
    return ('', 204)

@app.route("/api/order/<telno>")
def order(telno):
    telno = re.sub('[^0-9]','', telno)
    reader = csv.DictReader(open('data/order.csv', 'r'), delimiter = ',', quotechar="\"")
    for rec in reader:
        value = rec['number']
        if str(value) == str(telno):
            return rec
    return ('', 204)