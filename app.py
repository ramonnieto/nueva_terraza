import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify, send_from_directory, redirect

# Inicializa Firebase
cred = credentials.Certificate('./token_app_terraza.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Inicializa Flask
app = Flask(__name__, static_url_path='', static_folder='public')
mesa = 1  # iniciamos variable este valor vendra de QR
@app.route('/')
def serve_index():
    return send_from_directory('public', 'index.html')

@app.route('/thx')
def serve_thx():
    return send_from_directory('public', 'gracias.html')


@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json  # Obtiene los datos del cuerpo de la solicitud POST
    order_ref = db.collection('terraza').add(data)  # Añade los datos a la colección 'orders' en Firestore
    return jsonify({"status": "success", "order_id": order_ref[1].id}), 200  # Devuelve una respuesta JSON con el estado y el ID del pedido

if __name__ == '__main__':
    app.run(debug=True)
