from string import ascii_lowercase
import getpass

# contraseña mostrada usada para las pruebas 

# contrasena=input ("ingrese contraseña a validar \n").lower()

contrasena = getpass.getpass("Por favor, ingrese su contraseña: ").lower()
#variable para contar cantidad de intentos
contador =0

# ciclos correspondientes para recorrer los string 

for caracter in contrasena:
    for char in ascii_lowercase:
        # print(caracter,char)
        if caracter == char:
            contador =contador + 1
            break
        else:
            contador  =contador + 1


print(f"la cantidad de intentos fue: {contador} \n")      
  
print("---------------- fin del programa ----------------")