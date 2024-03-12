"""
Utilidades = P * U - GT 

P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

"""
Precio_suscripcion=float(input ("ingrese el Precio de la suscripción, debe ser un Numero mayor a 0 "))
numero_usuarios_Normales=float(input("ingrese la cantidad de usuarios considerados normales, debe ser un Numero mayor a 0 "))
gastos_totales =float(input("ingrese el valor de gastos totales "))
utilidades_ano_anterior=float(input("ingrese las utilidades del año anterior, estan debe ser mayor que 0 (cero)"))

utilidades =Precio_suscripcion*numero_usuarios_Normales  - gastos_totales
razon_utilidades= utilidades/utilidades_ano_anterior

print(f"las utiliades del año son {int(utilidades)} en pesos \n")
print(f"la razón de las utilidades entre este año y el anterior es: {razon_utilidades}")
