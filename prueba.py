import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
#from FirestoreDB import FirestoreClient
#db.collection('client').add(data) 

cred = credentials.Certificate("token_app_clinic.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

print("---------------------------")
print("Bienvenido a Clinica PePe")
print("---------------------------")
tipo_perfil=""  # iniciamos variable
# bucle para seccionar el perfil
while tipo_perfil != "client" and tipo_perfil != "doctor": # bucle para definir un perfil 
    tipo_perfil=input("Que perfil ejecutar un valor client o doctor: ")

# Perfil client
if tipo_perfil == "client":
    # se implementa el espacio cliente
    print("#######################")
    print("##  Espacio cliente ###")
    print("#######################") 
    dni=input("Dame un DNI: ")
    client=db.collection("dentista pruebas").document(dni).get().to_dict()
    if client is None:    # Si no existe el registro
        client=dict()
        client["name_client"]=input("Dame un nombre: ")
        client["apellido_client"]=input("Dame un apellido: ")
        client["telf_client"]=int(input("Dame un telf: "))
        db.collection("dentista pruebas").document(dni).set(client)
  
    print(client)    

    print (f"Bienvenido {client['name_client']} {client['apellido_client']}")
    #print ("Bienvenido " + client["name_client"] + " " + client["apellido_client"])
    while True:
        print("""
        Seleccione informacion que desea modificar:
        1. Nombre
        2. Apellido
        3. Telefono
        4. Email
        5. Localidad
        6. exit
        """)
        opcion = input("elige una opcion: ")
                
        if opcion == "6":
            exit()
        print(f"he elegido {opcion}")
        if opcion == "1":
            newname = input("Introduce nuevo nombre: ")
            db.collection("dentista pruebas").document(dni).update({"name_client": newname})
        if opcion == "2":
            newapellido = input("Introduce nuevo Apellido: ")
            db.collection("dentista pruebas").document(dni).update({"name_client": newapellido})
        if opcion == "3":
            newtelf = input("Introduce nuevo Apellido: ")
            db.collection("dentista pruebas").document(dni).update({"name_client": newtelf})
        if opcion == "4":
            newmail = input("Introduce nuevo Apellido: ")
            db.collection("dentista pruebas").document(dni).update({"name_client": newmail})
        if opcion == "5":
            newaddress = input("Introduce nuevo Apellido: ")
            db.collection("dentista pruebas").document(dni).update({"name_client": newaddress})
# Mejoras: el cliente puede consultar su historial
# perfil doctor
else:
    print("#######################")
    print("##  Espacio Doctor  ###")
    print("#######################")
    operation = "0"
    while True:
        print("""
        Seleccione informacion que desea modificar:
        1. Crear Doctor
        2. Buscar Doctor
        3. Actualizar Doctor
        4. Borrar Doctor
        5. exit
        """)
        opcion = input("elige una opcion: ")
                
        if opcion == "5":
            exit()
        print(f"he elegido {opcion}")
        if opcion == "1":
            dni=input("Introduzca el DNI: ")
            alta_client=db.collection("dentista pruebas").stream()
            for doc in alta_client:
                #print(f"{doc.id} => {doc.to_dict()}")
                if doc.id == dni:
                    print("El usuario existe")
            #print(alta_client)

            print(alta_client)
            if alta_client == dni:    # comprueba si existe
                print(f"El usuario con DNI {dni} ya existe")
        
        else:
            client=dict()
            client["name_client"]=input("Dame un nombre: ")
            client["apellido_client"]=input("Dame un apellido: ")
            client["telf_client"]=int(input("Dame un telf: "))
            db.collection("dentista pruebas").document(dni).set(client)
            #print(f"DNI: {alta_dni}, Apellido: {alta_apellido}, Nombre: {alta_name}")
# Registramos en la bbdd los datos de cliente
# db.child("clientes").push(client)
