"""
EJERCICIO 1

se le solicita a usted como programador el hecho de diseñar una
herramienta que permita determinar el estado nutricional de una persona.

"""
#VALORES ENTREGADOS POR EL USUARIO
peso_persona=float(input("ingrese el peso de la persona en KG\n"))
altura_persona=float(input("ingrese la altura de la persona en centimetros y distinto de cero (0) \n"))/100

if altura_persona == 0:
    print("la altura no puede ser igual a cero")
    
#CALCULO IMC
imc=round(peso_persona/pow(altura_persona,2),2)

#CLASIFICACIÓN SEGUN TABLA OMS

"""
< 18.5        Bajo Peso
[ 18.5,25 [   Adecuado
[ 25,  30 [   Sobrepeso
[ 30,  35 [   Obesidad Grado I
[ 35,  40 [   Obesidad Grado II
> 40          Obesidad Grado III
"""

if imc<18.5:
    print(f"su IMC es de {imc} y su clasificación según la OMS es de BAJO PESO\n")
elif imc >=18.5 and imc<25:
    print(f"su IMC es de {imc} y su clasificación según la OMS es de ADECUADO\n")
elif imc>=25 and imc <30:
    print(f"su IMC es de {imc} y su clasificación según la OMS es de SOBREPESO\n")
elif imc>=30 and imc <35:
    print(f"su IMC es de {imc} y su clasificación según la OMS es de OBESIDAD GRADO 1\n") 
elif imc>=35 and imc <40:
    print(f"su IMC es de {imc} y su clasificación según la OMS es de OBESIDAD GRADO 2\n") 
elif imc>=40:
    print(f"su IMC es de {imc} y su clasificación según la OMS es de OBESIDAD GRADO 3\n") 


print("TERMINO DEL PROGRAMA")