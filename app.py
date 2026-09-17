from flask import Flask, request, render_template, redirect, session
import sqlite3

from database import get_db, init_db

app = Flask(__name__)

# Vulnerability: hard-coded secret
app.secret_key = "mysecret123"

init_db()


@app.route("/")
def home():
    return """
    <h1>Task 3 - Secure Code Assessment</h1>
    <a href="/register">Register</a><br>
    <a href="/login">Login</a>
    """


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Vulnerability: plaintext password storage
        connection = get_db()

        connection.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        connection.commit()
        connection.close()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db()

        # Vulnerability: SQL query constructed using user input
        query = (
            "SELECT * FROM users WHERE username='"
            + username
            + "' AND password='"
            + password
            + "'"
        )

        user = connection.execute(query).fetchone()

        connection.close()

        if user:
            session["username"] = username
            return redirect("/dashboard")

        return "Invalid username or password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return "Access denied"

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


if __name__ == "__main__":
    app.run(debug=True)