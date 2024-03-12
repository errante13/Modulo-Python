from math import sqrt

radio = float(input("ingrese el radio en kilometros "))*1000
constante_g = float(input("ingrese la constante de gravedad (g) "))

velocidad_salida = sqrt(2*constante_g*radio)

print("La velocidad de Escape es ",round(velocidad_salida,1), "m/s")
