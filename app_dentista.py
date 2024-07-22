import pyrebase

# Configuración de Firebase
config = {
    "apiKey": "TU_API_KEY",
    "authDomain": "TU_DOMINIO.firebaseapp.com",
    "databaseURL": "https://TU_DOMINIO.firebaseio.com",
    "storageBucket": "TU_DOMINIO.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Función para registrar un cliente
def registrar_cliente(nombre, apellido, telefono):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }
    db.child("clientes").push(data)

# Función para registrar una intervención
def registrar_intervencion(id_cliente, intervencion):
    data = {
        "intervencion": intervencion
    }
    db.child("clientes").child(id_cliente).child("intervenciones").push(data)

# Función para obtener todos los clientes
def obtener_clientes():
    return db.child("clientes").get().val()

# Función para obtener las intervenciones de un cliente
def obtener_intervenciones(id_cliente):
    return db.child("clientes").child(id_cliente).child("intervenciones").get().val()

# Ejemplo de uso
if __name__ == "__main__":
    # Registro de cliente
    registrar_cliente("Juan", "Perez", "123456789")
   
    # Registro de intervención para un cliente
    clientes = obtener_clientes()
    id_primer_cliente = list(clientes.keys())[0]
    registrar_intervencion(id_primer_cliente, "Limpieza dental")
   
    # Obtención de todos los clientes
    print("Clientes:")
    print(obtener_clientes())
   
    # Obtención de las intervenciones de un cliente
    print("Intervenciones del primer cliente:")
    print(obtener_intervenciones(id_primer_cliente))
