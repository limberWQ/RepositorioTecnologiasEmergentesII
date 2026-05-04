from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///almacen.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)


#definiendo modelo
class Product(db.Model):
    __tablename__ = "Products"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    price = db.Column(db.Float, nullable = False)
    stock = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return f"product(name: '{self.name}', price: '{self.price}', stock: {self.stock})"
    

def init_database():
    with app.app_context():
        db.create_all()
        print("base de datos creada")




#CRUD
#Insertar productos
def insertar_productos():
    with app.app_context():

        # crear objetos
        producto1 = Product(name = "Monitor", price = "1500", stock = "40")
        producto2 = Product(name = "Mouse", price = "300", stock = "80")
        producto3 = Product(name = "teclado", price = "660", stock = "75")
        producto4 = Product(name = "MousePad", price = "100", stock = "120")

        #anhadir a la session
        db.session.add(producto1)
        db.session.add(producto2)
        db.session.add(producto3)
        db.session.add(producto4)


        #commit
        db.session.commit()
        print("Usuarios insertados")    

#Consultar tabla 
def consultar_tabla_productos():
    with app.app_context():
        #obtiene todos los registros
        print("Consulta todos los registros")
        todos = Product.query.all()
        for registro in todos:
            print(registro)

        #Obtiene registro filtrados (where)
        print("\nConsulta con WHERE")        
        filtrados = Product.query.filter(Product.id <= 2).all()
        for filtrado in filtrados:
            print(filtrado)

        print("\nConsulta de un solo registro")
        unico = Product.query.filter_by(id = 1).first()
        if unico:
            print(unico)


# Actualizar registros
def actualizar_registro():
    with app.app_context():
        registro = Product.query.filter_by(id=1).first()
        
        if registro:
            print(registro)
            registro.name = "Pantalla"

            db.session.commit()

            print("Registro actualizado correctamente")


# eliminar registro
def eliminar_registro():
    with app.app_context():
        registro = Product.query.filter_by(id = 4).first()

        if registro:
            db.session.delete(registro)

            db.session.commit()
            print("Registro eliminado correctamente")



if __name__ == "__main__":
    init_database()
    seleccion = input("Selecciona la opcion: ")
    match seleccion:
        case "1":
            insertar_productos()
        case "2":
            consultar_tabla_productos()        
        case "3":
            actualizar_registro()        
        case "4":    
            eliminar_registro()
