diccionario={
    "nombre":'Deiby',
    "edad":'19',
    "estatura":'1.75',
    "Ocupacion":'Estudiante',
    "Equipo favorito":'Nacional',
    "Cantante  favorito":'Luis Alberto Posada'
}
#Accediendo de forma individual a los atributos y valores en un diccionario
#print(diccionario['nombre'])
#print(diccionario.get('edad'))

#Acceder a Todos los atributos y valores de un diccionario al mismo tiempo
# recorrer un diccionario

for clave,valor in diccionario.items():
    print(clave,valor) 

diccionario["Hermanos"]= 1   
print(diccionario)