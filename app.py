from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_contact():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    notes = request.form["notes"]

    print(name)
    print(email)
    print(phone)
    print(notes)

    return "Contact Added"


if __name__ == "__main__":
    app.run(debug=True)