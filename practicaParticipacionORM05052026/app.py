from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

libro_genero = db.Table(
    "libro_genero",
    db.Column("libro_id", db.Integer, db.ForeignKey("libros.id"), primary_key=True),
    db.Column("genero_id", db.Integer, db.ForeignKey("generos.id"), primary_key=True)
)

#definicion de modelos libro, autor, genero
class Autor(db.Model):
    __tablename__ = "autores"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable = False)
    nacionalidad = db.Column(db.String(100), nullable=False)
    
    #relacion 1-N
    libros = db.relationship(
        "Libro",
        back_populates = "autor",
        cascade = "all, delete-orphan"
    )
    
    def __repr__(self):
        return f"Autor: {self.nombre}\nNacionalidad: {self.nacionalidad}"
    


# modelo Libro
class Libro(db.Model):
    __tablename__ = "libros"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable = False)
    anio = db.Column(db.Integer, nullable=False)
    # FK autor
    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), nullable=False)
    
    #Relacion con autor
    autor = db.relationship(
        "Autor",
        back_populates = "libros"
    ) 

    #relacion N - M  con genero
    generos = db.relationship(
        "Genero",
        secondary =libro_genero,
        back_populates = "libros"
    )
    
    def __repr__(self):
        return f"Titulo: {self.titulo}\nAño: {self.anio}"
    

# Modelo Genero
class Genero(db.Model):
    __tablename__ = "generos"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique = True)
    
    #relacion N - M
    libros = db.relationship(
        "Libro",
        secondary = libro_genero,
        back_populates = "generos"
    )
    
    def __repr__(self):
        return f"Nombre: {self.nombre}"
    
    

#crear DB
def init_database():
    with app.app_context():
        db.create_all()
        print("Base de datos creada correctamente")
#CRUD 
#INSERT       
def insertar_datos():
    with app.app_context():
        
        # AUTORES
        autor1 = Autor(
            nombre="Gabriel Garcia Marquez",
            nacionalidad="Colombiano"
        )

        autor2 = Autor(
            nombre="Isaac Asimov",
            nacionalidad="Ruso-Americano"
        )

        autor3 = Autor(
            nombre="Flor M. Salvador",
            nacionalidad="Mexicana"
        )


        # GENEROS
        genero1 = Genero(nombre="Ficción")
        genero2 = Genero(nombre="Ciencia")
        genero3 = Genero(nombre="Historia")
        genero4 = Genero(nombre="Romance Drama")


        # LIBROS
        libro1 = Libro(
            titulo="Cien años de soledad",
            anio=1967,
            autor=autor1
        )

        libro2 = Libro(
            titulo="Amor en los tiempos del colera",
            anio=1985,
            autor=autor1
        )

        libro3 = Libro(
            titulo="Fundacion",
            anio=1951,
            autor=autor2
        )

        libro4 = Libro(
            titulo="Boulevard",
            anio=2020,
            autor=autor3
        )

        db.session.add_all([
            autor1, autor2, autor3,
            genero1, genero2, genero3, genero4,
            libro1, libro2, libro3, libro4
        ])
        
        # ASOCIACIONES N-M
        libro1.generos.extend([genero1, genero3])
        libro2.generos.append(genero4)
        libro3.generos.extend([genero1, genero2])
        libro4.generos.append(genero4)
        
        db.session.commit()
        print("datos insertador correctamente")


#Consultar
def consultar_datos():
    with app.app_context():
        print("Listado de libros y autores\n")
        libros = Libro.query.all()
        
        for  libro in libros:
            print(libro)
            print(libro.autor)
            print("\n")
            
        print("\nListado de Autores y sus libros\n")
        autores = Autor.query.all()
        
        for autor in autores:
            print(autor)
            print(autor.libros)
            print("\n")
        
#actualizar

def actualizar_datos():
    with app.app_context():

        libro = Libro.query.filter_by(id=1).first()

        if libro:
            print(f"\nLibro actual: {libro.titulo}")

            libro.titulo = "Cien años de soledad (Edición Especial)"

            db.session.commit()

            print("Libro actualizado correctamente")


#eliminar
def eliminar_datos():
    with app.app_context():

        autor = Autor.query.filter_by(nombre="Isaac Asimov").first()

        if autor:
            db.session.delete(autor)
            db.session.commit()

            print("\nAutor eliminado correctamente")
            print("Sus libros también fueron eliminados")


# main
if __name__ == "__main__":
    #init_database()
    #insertar_datos()
    #consultar_datos
    #actualizar_datos()
    #eliminar_datos()
    consultar_datos()
        