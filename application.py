from cs50 import SQL
from flask import Flask, jsonify, render_template, request, redirect, url_for

application = Flask(__name__)

db = SQL("sqlite:///languages.db")

LANGUAGES = [
    "C",
    "Python",
    "JavaScript"
]

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/about")
def about():
    return render_template("about.html")

@application.route("/business")
def business():
    return render_template("business.html")

@application.route("/coding", methods=["GET", "POST"])
def coding():
    if request.method == "POST":
        language = request.form.get("language")
        db.execute("INSERT INTO languages (language) VALUES (?)", language)
        
        PYTHON = 0
        C_LANG = 0
        JAVA = 0

        python = db.execute("SELECT language FROM languages WHERE language = 'Python';")
        for row in range(len(python)):
            PYTHON += 1

        c = db.execute("SELECT language FROM languages WHERE language = 'C';")
        for row in range(len(c)):
            C_LANG += 1

        java = db.execute("SELECT language FROM languages WHERE language = 'JavaScript';")
        for row in range(len(java)):
            JAVA += 1

        return render_template("coding.html", python=PYTHON, c=C_LANG, java=JAVA, languages=LANGUAGES)
    
    else:
        PYTHON = 0
        C_LANG = 0
        JAVA = 0

        python = db.execute("SELECT language FROM languages WHERE language = 'Python';")
        for row in range(len(python)):
            PYTHON += 1

        c = db.execute("SELECT language FROM languages WHERE language = 'C';")
        for row in range(len(c)):
            C_LANG += 1

        java = db.execute("SELECT language FROM languages WHERE language = 'JavaScript';")
        for row in range(len(java)):
            JAVA += 1

        return render_template("coding.html", python=PYTHON, c=C_LANG, java=JAVA, languages=LANGUAGES)
    
@application.route("/contact")
def contact():
    return render_template("contact.html")
    