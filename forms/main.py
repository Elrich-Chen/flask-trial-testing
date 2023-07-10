from flask import Flask, render_template, flash, redirect, url_for, get_flashed_messages
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ergiualfnjvsoivhsdg'

@app.route("/")
def base():
    return render_template("layout.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"account successfully created for {form.username.data}!", 'success' )
        return redirect(url_for("base"))
    
    return render_template("register.html", title="Register", form = form)

@app.route('/Login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form = form)


if __name__ == "__main__":
    app.run(debug=True)