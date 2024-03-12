"""
Utilidades = P * U - GT 

P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

"""
Precio_suscripcion=float(input ("ingrese el Precio de la suscripción, debe ser un Numero mayor a 0 "))
numero_usuarios=float(input("ingrese la cantidad de usuarios, debe ser un Numero mayor a 0 "))
gastos_totales =float(input("ingrese el valor de gastos totales "))

utilidades =Precio_suscripcion*numero_usuarios - gastos_totales

print(f"las utiliades son {utilidades} en pesos")
