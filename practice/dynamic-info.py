from flask import Flask, redirect, render_template, url_for, request, session
from datetime import timedelta

app=Flask(__name__)
app.secret_key = "IUEEGUIEWBNGNESJKGBSJH"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/home")
def about():
    return render_template("home.html", title="HOME")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html", title="LOGIN")
    else:
        user_value = request.form["nm"]
        session.permanent=True
        session["user"] = user_value
        return redirect(url_for("user"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

