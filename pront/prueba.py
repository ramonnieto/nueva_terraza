print("Bienvenido a Clinica PePe")
tipo_perfil=""
while tipo_perfil != "client" and tipo_perfil != "doctor":
    tipo_perfil=input("Que perfil ejecutar un valor client o doctor: ")
"""     if tipo_perfil == "client":
        print("Hola soy un cliente")
    elif tipo_perfil =="doctor":
        print("Hola soy el doctor")
    else:
        print("seleccione un valor client o doctor") """

#print("Estoy fuera")


if tipo_perfil == "client":
    # se implementa el espacio cliente
    print("Hola soy un cliente")
    client = dict()
    client["name_client"]=input("Dame un nombre: ")
    client["apellido_client"]=input("Dame un apellido: ")
    client["telf_client"]=input("Dame un telf: ")
    print(client)
else:
    #~se implementa espacio doctor
    print("Hola soy el doctor")

