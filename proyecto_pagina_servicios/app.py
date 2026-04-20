from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    # Lista de servicios para pasar al HTML
    lista_servicios = [
        {"nombre": "Limpieza de Hogar", "img": "https://images.unsplash.com/photo-1527515545081-5db817172677?w=500", "desc": "Cuidado integral para salas, cocinas y dormitorios."},
        {"nombre": "Oficinas y Empresas", "img": "https://images.unsplash.com/photo-1556761175-4b46a572b786?w=500", "desc": "Mantenimiento profesional para espacios de trabajo."},
        {"nombre": "Limpieza de Ventanas", "img": "https://images.unsplash.com/photo-1527515862127-a4fc05baf7a5?w=500", "desc": "Acabado cristalino para interiores y exteriores."}]

    return render_template('servicios.html', servicios=lista_servicios)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    exito = False
    # Capturamos lo que viene de la otra página (si existe)
    servicio_preseleccionado = request.args.get('servicio_interes', '')
    
    if request.method == 'POST':
        exito = True
    return render_template('contacto.html', enviado=exito, preseleccion=servicio_preseleccionado)

if __name__ == '__main__':
    app.run(debug=True)