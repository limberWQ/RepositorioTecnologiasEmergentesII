from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [
    {
        'id':1, 
        'tarea':'Aprender flask',
        'completada':False
    },
    {
        'id':2,
        'tarea':'Practicar flask',
        'completada':False 
    }
]


#GET - obtener todas las tareas
@app.route("/api/tareas", methods = ['GET'])
def listar_tareas():
    return jsonify(tareas) 


#GET - obtener una tarea especifica
@app.route("/api/tareas/<int:tarea_id>", methods = ['GET'])
def obtener_tarea(tarea_id):
    tarea = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break 
    if tarea:
        return jsonify(tarea)
    return jsonify('Error: tarea no encontrada'), 404

#POST - creacion de una tarea
@app.route("/api/tareas", methods = ['POST'])
def crear_tarea():
    nueva_tarea = {
        'id':len(tareas)+1,
        'tarea':request.json.get('tarea',''),
        'completada':request.json.get('completada',False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea),201
#utilizar la herramienta reqbin.com
#instalar extension y enviar http://127.0.0.1:5000/api/tareas con GET 


#Eliminar tarea
@app.route("/api/tareas/<int:tarea_id>", methods = ['DELETE'])
def eliminar(tarea_id):
    global tareas
    tareas = [ t for t in tareas if t['id'] != tarea_id]
    return jsonify("mensaje: tarea eliminada"),200




if __name__ == "__main__":
    app.run(debug=True)