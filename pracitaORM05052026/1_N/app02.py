# Relación 1:N con Flask SQLAlchemy
# Un usuario puede tener muchas publicaciones (posts)
# Cada publicación pertenece a un solo usuario

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Crear la aplicación Flask
app = Flask(__name__)


# Configuración de la base de datos
# Se usará SQLite y se creará un archivo llamado blog.db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

# Desactiva notificaciones internas de cambios para ahorrar recursos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Inicializar SQLAlchemy para poder trabajar con ORM
db = SQLAlchemy(app)


# Modelo User
# Representa la tabla "users" en la base de datos
class User(db.Model):
    __tablename__ = "users"

    # Clave primaria: identifica de forma única a cada usuario
    id = db.Column(db.Integer, primary_key=True)

    # Nombre del usuario, obligatorio
    name = db.Column(db.String(50), nullable=False)

    # Correo del usuario, obligatorio y único (no se puede repetir)
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Relación con la tabla Post
    # Un usuario puede tener muchas publicaciones
    # "Post" es la clase relacionada
    # back_populates conecta esta relación con la variable "user" de Post
    # cascade hace que si se elimina un usuario, también se eliminen sus publicaciones
    posts = db.relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # Define cómo se mostrará un objeto User cuando se imprima
    def __repr__(self):
        return f"<user: {self.name}, email: {self.email}>"


# Modelo Post
# Representa la tabla "posts"
class Post(db.Model):
    __tablename__ = "posts"

    # Clave primaria de la publicación
    id = db.Column(db.Integer, primary_key=True)

    # Título de la publicación, obligatorio
    title = db.Column(db.String(100), nullable=False)

    # Contenido de la publicación, obligatorio
    content = db.Column(db.Text, nullable=False)

    # Llave foránea
    # Guarda el id del usuario dueño de esta publicación
    # Esto crea la relación 1:N en la base de datos
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Relación inversa
    # Permite acceder desde un post hacia su usuario
    # Ejemplo: post.user
    user = db.relationship("User", back_populates="posts")

    # Define cómo se mostrará un objeto Post al imprimirlo
    def __repr__(self):
        return f"POST: {self.title} | {self.user.name} | {self.user.email}"


# Función para crear las tablas en la base de datos
def init_database():
    with app.app_context():
        # Crea todas las tablas definidas por los modelos
        db.create_all()
        print("Base de datos creada correctamente")


# Función para insertar registros
def insertar_datos():
    with app.app_context():

        # Crear objetos usuario
        user1 = User(name="Limber Limachi", email="limber@gmail.com")
        user2 = User(name="Helen Mamani", email="helen@gmail.com")
        user3 = User(name="Miriam Limachi", email="miriam@gmail.com")

        # Crear publicaciones
        # user=user1 indica que el post pertenece a user1
        # SQLAlchemy automáticamente pondrá el user_id correcto
        post1 = Post(
            title="Primer post de Limber",
            content="Segunda publicacion",
            user=user1
        )

        post2 = Post(
            title="Segundo post de Limber",
            content="Primera publicacion",
            user=user1
        )

        post3 = Post(
            title="Primer post de Helen",
            content="Entrada uno de Helen",
            user=user2
        )

        post4 = Post(
            title="Primera entrada de Miriam",
            content="Entrada uno de Miriam",
            user=user3
        )

        # Agregar todos los objetos a la sesión
        # La sesión guarda temporalmente cambios antes de enviarlos a la BD
        db.session.add_all([
            user1, user2, user3,
            post1, post2, post3, post4
        ])

        # Guardar definitivamente en la base de datos
        db.session.commit()

        print("Usuarios y publicaciones insertadas")


# Función para consultar datos
def consultar_datos():
    with app.app_context():

        print("\nLista de usuarios y sus publicaciones:\n")

        # Obtener todos los usuarios de la tabla
        users = User.query.all()

        # Recorrer cada usuario
        for user in users:
            print(user)

            # user.posts obtiene automáticamente
            # todas las publicaciones relacionadas con ese usuario
            for entrada in user.posts:
                print(entrada)

            print()


# Función para actualizar un registro
def actualizar_datos():
    with app.app_context():

        print("\nActualizar publicación")

        # Buscar una publicación por id
        post = Post.query.filter_by(id=3).first()

        # Si existe, modificar su contenido
        if post:
            post.content = "Entrada actualizada de Helen"

            # Guardar cambios
            db.session.commit()

            print("Entrada actualizada correctamente")


# Función para eliminar registros
def eliminar_registro():
    with app.app_context():

        print("\nEliminar usuario en cascada")

        # Buscar usuario por id
        user = User.query.filter_by(id=1).first()

        if user:
            # Eliminar usuario
            db.session.delete(user)

            # Como tiene cascade, también se eliminan sus posts
            db.session.commit()

            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")


# Punto de inicio del programa
if __name__ == "__main__":

    # Crear tablas
    # init_database()

    # Insertar datos
    # insertar_datos()

    # Mostrar datos
    # consultar_datos()

    # Actualizar datos
    # actualizar_datos()

    # Eliminar usuario y sus posts
    #eliminar_registro()

    # Ver resultado final
    consultar_datos()