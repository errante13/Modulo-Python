from sys import argv
# argumento prueba
# 0.0046 0.093 0.0013 10000

print(" ------ INICIO ------ ")
#monedas

sol_peruano = float(argv[1])
peso_argentino =float(argv[2])
dolar_americano =float(argv[3])
peso_chileno = float(argv[4])

#conversiones 

print("")

print(f"Los {round(peso_chileno)} pesos equivalen a: ")
print(f"{sol_peruano*peso_chileno} Soles ")
print(f"{peso_argentino*peso_chileno} Pesos Argentinos ")
print(f"{dolar_americano*peso_chileno} Dólares ")

print("")
print(" ------ FIN ------ ")