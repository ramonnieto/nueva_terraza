import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
#from FirestoreDB import FirestoreClient
#db.collection('client').add(data) 

cred = credentials.Certificate("token_app_terraza.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

print("---------------------------")
print("Bienvenido a terraza PePe")
print("---------------------------")

mesa = 1  # iniciamos variable este valor vendra de QR

## Comento el acceso por cliente, ahora accedería por número de mesa en terraza (automatica)
#while tipo_perfil != "client" and tipo_perfil != "doctor": # bucle para definir un perfil 
#    tipo_perfil=input("Que perfil ejecutar un valor client o doctor: ")

if mesa == 1:
    # se implementa el espacio cliente
    print("#######################")
    print(f"## Su mesa es la número { mesa } ###") ## Deberá ser automatico delegado del QR
    print("#######################") 
    mesa_name=input("Dame un nombre para el pedido: ") ## Para pruebas lo pedimos
    mesa = "Mesa_" + str(mesa)
    client=db.collection("terraza").document(mesa).get().to_dict()
    if client is None:    # Si no existe el registro
        client=dict()
        client["racion_1"]=input("Qué primera ración quieres: ")
        client["racion_2"]=input("Qué segunda ración quieres ")
        client["racion_3"]=(input("Qué tercera ración quieres "))
        db.collection("terraza").document(mesa).set(client)
  
    print(client)    

    # Puede actualizar el pedido
    print (f"Ha pedido {client['racion_1']} {client['racion_2']} {client['racion_3']}, \n Gracias {mesa_name}")
    #print ("Bienvenido " + client["racion_1"] + " " + client["apellido_client"])
    while True:
        print(f"""
        Quiere cambiar su pedido ?:
        1. Pedido {client["racion_1"]}
        2. Pedido {client["racion_2"]}
        3. Pedido {client["racion_3"]}

        6. exit
        """)
        opcion = input("elige una opcion: ")
                
        if opcion == "6":
            exit()
        print(f"he elegido {opcion}")
        if opcion == "1":
            newname = input("Introduce nuevo nombre: ")
            db.collection("terraza").document(mesa).update({"racion_1": newname})
        if opcion == "2":
            newapellido = input("Introduce nuevo Apellido: ")
            db.collection("terraza").document(mesa).update({"racion_2": newapellido})
        if opcion == "3":
            newtelf = input("Introduce nuevo Apellido: ")
            db.collection("terraza").document(mesa).update({"racion_3": newtelf})

# Mejoras: el cliente puede consultar su historial de pedidos
