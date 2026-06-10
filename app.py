from flask import Flask, render_template, request
import csv
import os
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "data/students.csv"

# CSV file create if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Name",
            "Phone",
            "Email",
            "Age",
            "Interest",
            "Date",
            "Status"
        ])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    age = request.form["age"]
    interest = request.form["interest"]

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            phone,
            email,
            age,
            interest,
            datetime.now().strftime("%d-%m-%Y %H:%M"),
            "New Lead"
        ])

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
