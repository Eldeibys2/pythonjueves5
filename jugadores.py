opcion=100
i=0


print("***Empanadas Inteligentes***")
print("1.Agregar cliente: ")
print("2.mOSTRAR  cliente: ")
print("3.Buscar un cliente por cedular: ")
print("4.Como eliminar a un cliente por medio de la ce ")
print("0.salir")


clientes=[]

while(opcion !=0):

    cliente={}
    opcion=int(input('Digite la opcion preferida: '))

    #Caminos del menu
    if(opcion==1):
        cliente['cedula'] = input("Digite su cedula: ")
        cliente['nombre'] = input("Digite su nombre: ")
        clientes.insert(i,cliente)
        i = i+1

    elif(opcion==2):
         print(cliente)   

    elif(opcion==3):
         cedulaAbuscar = input("Digite la cedula")
         for cliente in clientes:
            if(cliente["cedula"]==cedulaAbuscar):
                print(f"Cliente encontrado: {cliente['cedula']}")
            else:
                print("Usuario no encontrado")    


    elif(opcion==0):
        break


    else:
        print("Digite una opcion disponible")    


else:
    print("Adios")    
