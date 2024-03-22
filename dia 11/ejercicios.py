notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
}

print (notas)#imprime todo
print (len(notas))# imprime el tamaño

#print(notas[2]) #error
#print (notas["FElipe"]) #error

print(notas.get("FElipe"))#none
print(notas.get("felipe"))#6 
print(notas.get("Camila"))#7
print(notas.get("mijail","valor no encontrado")) 

prueba = notas.get("julio")
print(prueba)#none
print(type(prueba))#<class 'noneType'>

#set default cuando la clave existe, devuelve el valor actual. no lo reemplaza
notas.setdefault("luis",10)
print(notas)

notas.setdefault("valeria")

### tuplas son similares a las listas y son inmutables se escriben en ()

###Comparar diccionarios
dic1 = {1:"uno",2:"dos"}
dic2 = {2:"dos",1:"uno"}
dic3 = {2:"dos",3:"tres"}
dic4 = {2:"dos",3:"cuatro"}
print(dic1==dic2) #True
print(dic1==dic3) #False
print(dic4==dic3) #False

pares_impares ={
    "pares":{2:"dos", 4: "cuatro", 6:"seis",8:"ocho",10:"diez"},
    "impar":{"uno":1,"tres":3,"cinco":5,"siete":7,"nueve":9}
}
print("")
print (pares_impares["pares"][6])
print (pares_impares["impar"]["cinco"])