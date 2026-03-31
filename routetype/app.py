from flask import Flask

app = Flask(__name__)

#Rutas con parámetros que tienen explícito el tipo de dato
@app.route("/cadena/<string:nombre>")
def demo_cadena(nombre):
    return f"Cadena: {nombre} -> Tipo de dato: {type(nombre).__name__}"

@app.route("/entero/<int:numero>")
def demo_entero(numero):
    return f"Entero: {numero} -> Tipo de dato: {type(numero).__name__}"

@app.route("/decimal/<float:decimal>")
def demo_float(decimal):
    return f"Float recibido: {decimal} -> Tipo de dato: {type(decimal).__name__}"

#Podemos enviar una ruta para usarla como parámetro (path es el tipo y ruta es el nombre del parámetro)
#Solo se va a mostrar el nombre de la ruta, no su contenido
@app.route("/ruta/<path:ruta>")
def demo_ruta(ruta):
    return f"Ruta: {ruta}"

if __name__ == "__main__":
    app.run(debug = True)