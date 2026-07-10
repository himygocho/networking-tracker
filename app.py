import csv
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "contacts.csv")


@app.route("/")
def home():

    contacts = []

    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                contacts.append(row)

    except FileNotFoundError:
        pass

    return render_template(
        "index.html",
        contacts=contacts
    )

@app.route("/add", methods=["POST"])
def add_contact():

    print(os.getcwd())
    print(os.path.abspath("contacts.csv"))

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    notes = request.form["notes"]

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            name,
            email,
            phone,
            notes
        ])

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)