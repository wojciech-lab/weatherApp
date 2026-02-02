from flask import Flask, render_template
from datetime import datetime
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
    return render_template("conctact.html",
                           nr_tel=phone,
                           adres_email=email)


@app.route("/wiadomosci/<title>")
def news_page(title: str):
    return "Strona wiadomości {title.capitalize()}"


