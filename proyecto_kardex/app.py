from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
def init_database():
    conn = sqlite3.connect("kardex.db")
    
    conn.execute(
        """
        create table if not exists personas(
            id integer primary key,
            nombre text not null,
            telefono text not null,
            fecha_nacimiento date not null
        )
        """
    )
    conn.commit()
    conn.close()
    
init_database()

# def obtener_persona_por_id(id):
#     conn = sqlite3.connect("kardex.db")
#     conn.row_factory = sqlite3.Row
    
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM personas WHERE id = ?", (id,))
#     persona = cursor.fetchall()  
    
#     return persona


# persona = obtener_persona_por_id(1)
# for i in persona:
#     print(i['nombre'], i['telefono'], i['fecha_nacimiento'])

#listado de registros
@app.route("/")
def index():
    conn = sqlite3.connect("kardex.db")
    
    # permite manejar registros en forma de diccionario
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("select * from personas")
    personas = cursor.fetchall()
    return render_template('index.html', personas = personas)

    
#registro nuevo
@app.route("/create")
def create():
    return render_template('create.html')

# guardar registro nuevo
@app.route("/save", methods = ['POST'])
def save():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha_nacimiento = request.form['fecha_nacimiento']
    
    conn = sqlite3.connect("kardex.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        insert into personas (nombre,telefono,fecha_nacimiento)
        values(?,?,?)
        """,
        (nombre, telefono, fecha_nacimiento))
    conn.commit()
    conn.close()
    return redirect('/')

# editar registro
@app.route("/edit/<int:id>")
def persona_id(id):
    conn = sqlite3.connect("kardex.db")
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("select * from personas where id = ?", (id,))
    persona = cursor.fetchone()
    conn.close
    return render_template('edit.html', persona = persona)

# Guardar actualizacion de registro
@app.route("/update", methods = ['POST'])
def personas_update():
    id = request.form['id']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha_nacimiento = request.form['fecha_nacimiento']
    
    conn = sqlite3.connect("kardex.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        update personas set nombre=?, telefono=?, fecha_nacimiento=? where id =?
        """,(nombre, telefono, fecha_nacimiento, id))
    conn.commit()
    conn.close()
    return redirect('/')
    
# eliminar registro
@app.route("/delete/<int:id>")
def personas_delete(id):
    conn = sqlite3.connect("kardex.db")
    cursor = conn.cursor()
    cursor.execute("delete from personas where id=?",(id,))
    conn.commit()
    conn.close()
    return redirect('/')

    
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)