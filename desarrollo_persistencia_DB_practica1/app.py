import sqlite3

conn = sqlite3.connect("instituto.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS cursos(
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        horas INTEGER NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS estudiantes(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL
    )
    """
)

conn.execute(
    """
    create table if not exists inscripciones(
        id integer primary key,
        fecha text not null,
        curso_id integer not null,
        estudiante_id integer not null,
        FOREIGN KEY (curso_id) references cursos(id),
        FOREIGN KEY (estudiante_id) references estudiantes(id)
    )
    """
)


# conn.execute(
#     """
#     insert into inscripciones(fecha, curso_id, estudiante_id)
#     values ('2026-04-14',1,1)
#     """
# )
# conn.execute(
#     """
#     insert into inscripciones(fecha, curso_id, estudiante_id)
#     values ('2026-04-14',2,1)
#     """
# )


# conn.execute(
#     """
#     INSERT INTO cursos (descripcion, horas)
#     VALUES ('De cero a experto',40)
#     """
# )

# conn.execute(
#     """
#     INSERT INTO estudiantes (nombre, apellidos, fecha_nacimiento)
#     VALUES ('Limber','Limachi Quispe','2002-08-22')
#     """
# )
#conn.commit()


# consulta y guardar en cursos para mostrar datos
print("datos cursos")
cursor = conn.execute("select * from cursos")
for row in cursor:
    print(row)

print("\ndatos estudiantes")
cursor = conn.execute("select * from estudiantes")

for fila in cursor:
    print(fila)
print("\ndatos inscripciones")
cursor = conn.execute("select * from inscripciones")
for item in cursor:
    print(item)