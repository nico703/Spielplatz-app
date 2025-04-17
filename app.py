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

        # In CSV schreiben
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, item])

        return redirect("/")

    # Einträge aus CSV lesen
    guests = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline="") as f:
            reader = csv.reader(f)
            guests = list(reader)

    return render_template("index.html", guests=guests)

if __name__ == "__main__":
    app.run(debug=True)
