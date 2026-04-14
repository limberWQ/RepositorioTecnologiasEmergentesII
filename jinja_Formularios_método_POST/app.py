from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return redirect(url_for("user", user=nombre))
    else:
        return render_template("login.html")


@app.route("/<user>")
def user(user):
    return f"<h1>{user}</h1>"

if __name__ == "__main__":
    app.run(debug=True)