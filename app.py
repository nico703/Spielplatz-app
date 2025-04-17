from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
CSV_FILE = "guests.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        item = request.form["item"]

        # Bisherige Einträge lesen
        guests = []
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, newline="") as f:
                reader = csv.reader(f)
                guests = list(reader)

        # Prüfen, ob Item schon vergeben ist (groß/klein ignorieren)
        if any(item.lower() == existing[1].lower() for existing in guests):
            return render_template("index.html", guests=guests, error=f"'{item}' wurde schon eingetragen!")

        # Eintrag speichern
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, item])

        return redirect("/")

    # Einträge laden
    guests = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline="") as f:
            reader = csv.reader(f)
            guests = list(reader)

    return render_template("index.html", guests=guests, error=None)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)