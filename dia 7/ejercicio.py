#sentencias iterativas 

import getpass

password =getpass.getpass("ingrese la clave secreta")

print(f"la clave es {password}")

while password != "hola mundo":
    password = getpass.getpass("ingrese la clave secreta")
    
print("saliste del ciclo")

#ciclo while 
inicio = 0
fin = 6

while inicio < fin:
    print(f" inicio {inicio} , fin {fin}")
    inicio = inicio + 1
    
print("fin del while")

#ITERACIONES 

