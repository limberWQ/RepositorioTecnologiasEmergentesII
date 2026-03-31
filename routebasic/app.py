from flask import Flask

app = Flask(__name__)

#Las rutas básicas se agregan usando el @app.route
@app.route("/")
def inicio():
    return "<h1>Página de inicio</h1>"

@app.route("/acerca-de")
def acerca_de():
    return "<h1>Información sobre nosotros</h1>"

@app.route("/contacto-de")
def contacto():
    return "<h1>Página de contacto</h1>"

#Podemos usar una función asociada a varias rutas
@app.route("/info")
@app.route("/informacion")
@app.route("/about")
def informacion():
    return "<h1>Página de información</h1>"

if __name__ == "__main__":
    app.run(debug = True)