#importación librerias
from sys import argv

#diccionario a revisar
ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}
#valor entregado para validar las referencias por argumento
referencia= int(argv[1])
#creacion de nueva lista con el filtrado correspondiente
entrega = {clave:valor for clave,valor in ventas.items() if valor >referencia}

#impresión del nuevo diccionario
print(f"estos son los meses con ventas mayores a {referencia} \n {entrega}")
