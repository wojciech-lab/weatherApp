from flask import Flask, render_template, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    year = datetime.now().year
    cities = ["Warszawa","Kraków","Berlin"]
    admin = True
    return render_template("index.html",
                           rok=year,
                           miasto=cities,
                           admin=admin
    )


@app.route("/kontakt")
def contact_page():
    phone = "44141231551"
    email = "firma@firma.pl"
    return render_template(
        "conctact.html",
                           nr_tel=phone,
                           adres_email=email
    )


@app.route("/wiadomosci/<title>")
def news_page(title: str):
    return "Strona wiadomości {title.capitalize()}"

@app.route("/panstwa")
def al_countries_page():
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags,cca3")
    data = response.json()
    return render_template(
        "countries.html",
                           countries=data



                           )

@app.route("/panstwa/kraj/<cca3>")
def single_country(cca3):

    response = requests.get(f"https://restcountries.com/v3.1/alpha/{cca3}")
    data = response.json()

    return render_template(
        "details.html",
        country=data[0]

    )
