from flask import Flask, render_template, url_for, redirect, request
import sqlite3

app = Flask(__name__)

def init_database():
    conn = sqlite3.connect("practica.db")
    
    conn.execute(
        """
        create table if not exists estudiante(
            id integer primary key,
            nombre text not null,
            apellido_pat text not null,
            apellido_mat text not null,
            celular integer not null
        );
        """   
    )
    
    conn.execute(
        """
        create table if not exists curso(
            id integer primary key,
            curso_nombre text not null,
            descripcion text not null 
        );
        """
    )
    
    conn.execute(
        """
        create table if not exists inscripciones(
            id integer primary key,
            id_curso,
            id_estudiante,
            foreign key (id_curso) references curso(id),
            foreign key (id_estudiante) references estudiante(id)  
        );
        """
    )
    
    
        
    conn.commit()
    conn.close()
    
    
init_database()

@app.route("/")
def index():
    conn = sqlite3.connect("practica.db")
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    
    cursor.execute("select * from estudiante")
    personas = cursor.fetchall()
    
    return render_template('index.html', personas = personas)




    
@app.route("/create")
def create():
    return render_template('create.html')

####insertar estudiantes en tabla estudiante base de datos
@app.route("/insertar", methods =['POST'])
def insertarestudiantes():
    
    nombre = request.form['nombre']
    apellido_pat = request.form['apellido_pat']
    apellido_mat = request.form['apellido_mat']
    celular = request.form['celular']
    
    conn = sqlite3.connect("practica.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        insert into estudiante (nombre,apellido_pat,apellido_mat,celular)
        values (?,?,?,?)
        """,
        (nombre, apellido_pat, apellido_mat, celular)
    )
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/create_curso")
def create_curso():
    return render_template('create_curso.html')
#crear curso
@app.route("/insertar_curso", methods = ['POST'])
def insertar_curso():
    curso_nombre = request.form['curso_nombre']
    descripcion = request.form['descripcion']
    
    conn = sqlite3.connect("practica.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        insert into curso (curso_nombre,descripcion)
        values(?,?)
        """,
        (curso_nombre, descripcion)
    )
    conn.commit()
    conn.close()
    return redirect("/")


### insertar cursos
@app.route("/inscripciones")
def inscripciones():
    conn = sqlite3.connect("practica.db")
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    
    cursor.execute("select id, nombre, celular from estudiante")
    lista = cursor.fetchall()
    return render_template('inscribir_curso.html', lista = lista)


@app.route("/edicion")
def edicion():
    return render_template('editar.html')

@app.route("/edicion_estudiante/<int:id>", methods = ['GET', 'POST'])
def edicion_estudiante(id):
    conn = sqlite3.connect("practica.db")
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    
@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = sqlite3.connect("practica.db")
    cursor = conn.cursor()
    
    
    cursor.execute("delete from estudiante where id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)