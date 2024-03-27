def imprimir_menu():
    print("Opciones: ")
    print("1). De acuerdo")
    print("2). En desacuerdo")
    print("3). No me interesa")

preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []

for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input("> "))
    print("")
    
for i in range(len(respuestas)):  #[0,1,2]   len = 3  
    print(f"La respuesta a la pregunta {i+1} es: {respuestas[i]}")
    
    

def suma(valor1,valor2):#valor1=3 ; valor2=5
    suma = valor1 + valor2 # suma= 3 + 5; suma = 8
    return suma #return 8

suma(3,5)

print("valor de respuesta",suma(1,9))#se imprime el valor de retorno

resultado = suma(6,7)#capturando el valor de retorno
print("valor respuesta capturado",resultado)#imprimiendo el valor de retorno