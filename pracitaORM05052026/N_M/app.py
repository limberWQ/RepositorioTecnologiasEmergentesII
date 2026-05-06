from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#definicion de modelos n-m 
#tabla intermedia
student_course = db.Table(
    "student_course",
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True)
)

class Student(db.Model):
    __tablename__ = "students"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    #relacion de cursos de la tabla estudiante con la tabla intermedia
    courses = db.relationship("Course", secondary=student_course, back_populates = "students")
    
    def __repr__(self):
        return f"<Estudiante: Nombre={self.name}>"
    
class Course(db.Model):
    __tablename__ = "courses"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    
    students = db.relationship("Student", secondary=student_course, back_populates="courses")
    
    def __repr__(self):
        return f"<Cursos: Titulo={self.title}>"
    

#funcion para iniciar la base de datos
def init_database():
    with app.app_context():
        db.create_all()
        print("Base de datos creado satisfactoriamente")
        

#insertar registros
def insertar_datos():
    with app.app_context():
        estudiante1 = Student(name="Limber Limachi")
        estudiante2 = Student(name="Wendy Vargas")
        estudiante3 = Student(name="Miriam Limachi")
        
        #crear objetos cursos
        curso1 = Course(title="Python")
        curso2 = Course(title="JS")
        curso3 = Course(title="C++")
        
        db.session.add_all([estudiante1,estudiante2,estudiante3, 
                            curso1,curso2,curso3])
        
        #registro de un estudiante a dos cursos o mas con una lista EXTEND
        estudiante1.courses.extend([curso1,curso2])
        
        #registro de un estuantes a un solo curso APPEND
        estudiante2.courses.append(curso2)
        
        estudiante3.courses.extend([curso1,curso3])
        
        db.session.commit()
        print("Estudiantes y cursos insertados correctamente")
        
#Consulta
def consultar_datos():
    with app.app_context():
        print("\nListado de estudiantes y cursos")
        students = Student.query.all()
        
        for student in students:
            print(student)
            for c in student.courses:
                print(f"-{c.title}")
            print("\n")
        
        print("\nListado de cursos y estudiantes")
        courses = Course.query.all()
        
        for course in courses:
            print(f"{course} tiene inscritos a: ")
            for e in course.students:
                print(f"Nombre: {e.name}")
            print("\n")
        
#Actualizar
def actualizar_relaciones():
    with app.app_context():
        print("\nAgregando un curso a un estudiante")
        estudiante = Student.query.filter_by(id=1).first()
        curso = Course.query.filter_by(id=3).first()
        
        if estudiante and curso:
            estudiante.courses.append(curso)
            db.session.commit()
            print("Inscripcion actualizada")
        else:
            print("no hay datos")

#
def eliminar_relaciones():
    with app.app_context():
        estudiante = Student.query.filter_by(id=1).first()
        curso = Course.query.filter_by(id=3).first()
        
        if estudiante and curso:
            estudiante.courses.remove(curso)
            db.session.commit()
            print("se elimino la inscripcion")
            
            
if __name__ == "__main__":
    # init_database()
    # insertar_datos()
    #actualizar_relaciones()  
    eliminar_relaciones()  
    consultar_datos()