from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app_name': 'Capstone Project Server',
        'version': '1.0',
        'description': 'Servidor basico con rutas GET y POST.'
    })

@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    if not data or 'mensaje' not in data:
        return jsonify({'error': 'Falta el campo "mensaje" en el cuerpo JSON'}), 400

    mensaje_usuario = data['mensaje']
    respuesta = f"Hola, recibí tu mensaje: '{mensaje_usuario}'"
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)
