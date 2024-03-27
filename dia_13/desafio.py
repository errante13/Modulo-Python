#Calculo del factorial de un numero

def factorial(numero):#5! = 5*4*3*2*1
    valor = 1 # variable acumuladora
    for n in range(1,numero+1):#1,2,3,4,5
        valor = valor * n
    return valor

factorial(5)
