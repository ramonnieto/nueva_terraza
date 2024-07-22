#print("CASE 1:  When we need to take two inputs at a time")
#print statement


doctor_datos = list(map(str, input("Intruduzca nombre del doctor: ").split()))

client_datos = list(map(str, input("Intruduzca nombre, apellido, telf del cliente: ").split()))

print("Nombre Doctor: ", doctor_datos[0])  
print("Nombre Client: ", client_datos[0])
print("Apellido Client: ", client_datos[1])
print("Telf Client: ", client_datos[2])