from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proceso", methods=["POST"])
def proceso():
    # nombre
    nombre = request.form.get("nombre")
    # lista
    lenguajes = request.form.getlist("lenguajes")
    return render_template("salida.html", nombre = nombre, lenguajes = lenguajes)

if __name__ == "__main__":
    app.run(debug=True)