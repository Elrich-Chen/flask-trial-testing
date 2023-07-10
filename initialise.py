from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

names=["tom", "Jerry", "bruh"]

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/test")
def test():
    return render_template("index.html")


if __name__== '__main__' :
    app.run(debug=True)