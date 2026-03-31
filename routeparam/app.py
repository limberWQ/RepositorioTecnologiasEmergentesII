from flask import Flask

app = Flask(__name__)

#Para poner parámetros necesitamos poner entre /<>
@app.route("/usuario/<nombre>")
#ponemos el parámetro que estamos recibiendo como parámetro de la función (con el mismo nombre)
def perfil_usuario(nombre):
    return f"Perfil de: <strong>{nombre}</strong>"

@app.route("/post/<id>")
def ver_post(id):
    return f"Mostrando el post: <strong>{id}</strong>"

#Para agregar más parámetros solo lo separamos con /
@app.route("/categoria/<categoria>/<producto>")
def productos(categoria,producto):
    return f"Categoría: <strong>{categoria}</strong>, Producto: <strong>{producto}</strong>"

if __name__ == "__main__":
    app.run(debug = True)