import os
from flask import Flask, render_template, request, redirect
from database import init_db, get_guests, add_guest, item_exists

app = Flask(__name__)

# Datenbank initialisieren
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        item = request.form["item"]

        # Check ob Item schon vergeben ist
        if item_exists(item):
            guests = get_guests()
            return render_template("index.html", guests=guests, error=f"'{item}' wurde schon eingetragen!")

        add_guest(name, item)
        return redirect("/")

    guests = get_guests()
    return render_template("index.html", guests=guests, error=None)
