"""
Para poner en práctica lo que hemos aprendido a lo largo de la unidad, se implementará un
programa en Python que permite jugar al cachipún en contra del computador.

"""
#import libreria random
import random
# import de argv para uso de linea de comando
from sys import argv

#creación de una opción aleatoria para el pc
computador=random.choice(['piedra','papel','tijera'])

#seleccion_usuario=input("ingrese piedra, papel o tijeras para comenzar a juegar \n").lower()
#entrega de datos por linea de comandos 
seleccion_usuario=argv[1].lower()

#validación de datos del usuario
# if seleccion_usuario =="piedra":
#     print(f"tu jugaste: {seleccion_usuario}")
# elif seleccion_usuario =="tijera":
#     print(f"tu jugaste: {seleccion_usuario}")
# elif seleccion_usuario =="papel":
#     print(f"tu jugaste: {seleccion_usuario}")
# else:
#     print("la opción escogida es INVALIDAD, favor es cojer entre piedra, papel o tijera\n")    

if seleccion_usuario != "piedra" and seleccion_usuario != "papel" and seleccion_usuario != "tijera":
     print("la opción escogida es INVALIDAD, favor es cojer entre piedra, papel o tijera\n") 
else:
    """
    POSIBLES CONVINACIONES 
    PC    USER 
    "PIEDRA PIEDRA "
    PIEDRA TIJERA--
    PIEDRA PAPEL--
    "TIJERA TIJERA" 
    TIJERA PAPEL --
    TIJERA PIEDRA--
    "PEPEL PAPEL"
    PAPEL PIEDRA--
    PAPEL TIJERAS-- 
    """

    # piedra tijeras    
    if computador =="piedra"and seleccion_usuario=="tijera":
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n ")
        print("PERDISTE piedra rompe tijeras\n")
    #papel tijeras   
    elif computador =="papel"and seleccion_usuario=="piedra":
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n ")
        print("PERDISTE papel envuelve a piedra\n")
    #tijeras papel   
    elif computador =="tijera" and seleccion_usuario=="papel":
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n ")
        print("PERDISTE tijeras cortan papel\n")
    #piedra papel
    elif computador =="piedra"and seleccion_usuario=="papel":
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n")
        print("GANASTE papel envuelve a piedra\n")
    #tijera piedra
    elif computador =="tijera"and seleccion_usuario=="piedra":
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n ")
        print("GANASTE piedra rompe tijera\n")
    #papel piedra
    elif computador =="papel"and seleccion_usuario=="tijera":
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n ")
        print("GANASTE tijera cortan papel\n")
    #caso de empate
    elif computador==seleccion_usuario:
        print(f"El computador eligió: {computador}\n")
        print(f"Tu jusgaste {seleccion_usuario}\n ")
        print("es un EMPATE \n")

print("fin del juego")    