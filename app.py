from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos simulados
todos = {"todos": ["Estudiar", "Comer", "Jugar"]}

# Ruta 1: Información de la app
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "app": "Servidor Capstone",
        "versión": "1.0",
        "autor": "Tu nombre aquí",
        "descripción": "API de ejemplo para proyecto Capstone"
    })

# Ruta 2: POST /mensaje
@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    if not data or "mensaje" not in data:
        return jsonify({"error": "Se requiere el campo 'mensaje'"}), 400

    mensaje_usuario = data["mensaje"]
    respuesta = f"Hola, recibí tu mensaje: '{mensaje_usuario}' ¡Gracias por enviarlo!"
    
    return jsonify({"respuesta": respuesta})


if __name__ == "__main__":
    app.run(debug=True)
