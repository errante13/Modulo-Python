"""
Dia 2: Tipos de datos:

son formas de mostrar datos, existen dos tipos, numericos y string
dentro de los numericos existen dos integer y float

la separación de float es un punto (.)

la división de integer es un float siempre 

String format 

las VARIABLES siempre comenzarán en minusculas y de ser más de una palabra se usa _ para unirlas
(nombre_variable)o  la siguiente  letra de la palabra en mayusculas (nombreVariable) no pueden
comenzar con numeros ni contener espacio 

"""
#STRING FORMAT 
nombre="luis"
año= '2024'
mes=3
dia=8
verdadero=True
print ("hola {}, el año es {}, del mes {} y el día es {} ".format(nombre, año, mes,dia))
print (2/1)#división de enteros da float 

print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))#interpolación con % 
# %s para String y %d para numeros

#metodo count (contar un caracter en una cadena)
print ("luis".count("u"))

#metodos upper y lower (para poner mayusculas o minusculas como corresponda)
print("eRRantE, metodo upper (texto en mayusculas)".upper())
print("eRRantE, metodo lower (texto en minusculas)".lower())
#metodo title (coloca la primera en mayusculas)
print("eRRantE, metodo title, pone la primera letra en mayusculas y el resto en mayusculas",nombre.title())

#len() es una función necesita una variable dentro (cuenta los caracteres incluye espacio)
print(len("Luis lagos carrera"))

#Join() permite unir muchos elementos separados por un string
print(", ".join(["a","b","c"]))

#\n para saltos de linea o para imprimir en más de una linea (funciona similar que println)

print(" esto \n es \n un \n salto \n de \n linea")

#type sirve para indentificar el tipo de valor de una variable si es numerica o string
print(type(nombre))#<class 'str'>
print(type(mes))  #<class 'int'>
print(type(año))#<class 'str'>
print(type(verdadero))#<class 'bool'>

type(nombre)#esto no imrprime el tipo de dato

#precisión de datos
print (f"el reesultado es {9/7:.4f}")
print (round((9/7), 3))

nombre= input("ingresa tu nombre ")
print ("tu nombre es: ",nombre)
print(type(nombre))