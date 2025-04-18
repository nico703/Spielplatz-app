from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Guest
import os

app = Flask(__name__)

# Datenbank-Konfiguration
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///guests.db")  # lokal SQLite fallback
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        item = request.form["item"]

        # Prüfen ob das Item schon vergeben ist
        if Guest.query.filter(db.func.lower(Guest.item) == item.lower()).first():
            guests = Guest.query.all()
            return render_template("index.html", guests=guests, error=f"'{item}' wurde schon eingetragen!")

        # Neuen Eintrag speichern
        new_guest = Guest(name=name, item=item)
        db.session.add(new_guest)
        db.session.commit()

        return redirect("/")

    guests = Guest.query.all()
    return render_template("index.html", guests=guests, error=None)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)