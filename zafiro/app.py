from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_database():
    conn = sqlite3.connect("registro.db")
    conn.execute(
        """
        create table if not exists notas(
            id integer primary key, 
            nombre text not null,
            nota number not null
        );
        """
    )
    conn.commit()
    conn.close()

init_database()



@app.route("/")
def index():
    conn = sqlite3.connect("registro.db")
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute(
        """
        select * from notas;
        """
    )
    
    lista = cursor.fetchall()
    
    return render_template('index.html', lista = lista)


@app.route("/crear")
def crear():
    return render_template('crear.html')

@app.route("/registro", methods=['POST'])
def registro():
    conn = sqlite3.connect("registro.db")
    
    nombre = request.form['nombre']
    nota = request.form['nota']
    
    conn.execute(
        """
        insert into notas (nombre,nota) 
        values (?,?);
        """,(nombre, nota)
    )
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = sqlite3.connect("registro.db")
    conn.execute("delete from notas where id=?",(id,))
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route("/editar/<int:id>")
def editar(id):
    conn = sqlite3.connect("registro.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("select * from notas where id = ?", (id,))
    
    nombre = cursor.fetchone()
    conn.close()
    return render_template('editar.html', nombre = nombre)

@app.route("/update", methods=['POST'])
def update():
    print("verificar")
    conn = sqlite3.connect("registro.db")
    
    id = request.form['id']
    nombre = request.form['nombre']
    nota = request.form['nota']
    
    cursor = conn.cursor()
    
    cursor.execute(
        """
        update notas set nombre=?, nota=? where id=?
        """,(nombre, nota, id)
    )
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)