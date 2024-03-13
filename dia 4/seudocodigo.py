"""
solicitar al usuario en ingreso de 3 numeros y 
determinar cuales de ellos es mayor que 33
solo numeros enteros 1 al 100
y determinar cual es mayor y cual es menor
"""
"""
1 ingresar numeros ("ingrese 3 números que sean enteros y que estén entre 1 y 100)
pregunta -> son numeros enteros
    no> volver al paso 1 
    si> preguntar -> está entre 1 y 100 
        si> continuar al siguiente paso
        no> volver al paso 1
2 pregunta -> número 1 es > 33 
    si> mostrar mensaje de que numero 1 es mayor que 33
    no> mostrar mensaje de que numero 1 no es mayor que 33 
3 pregunta -> número 2 es > 33 
    si> mostrar mensaje de que numero 2 es mayor que 33
    no> mostrar mensaje de que numero 2 no es mayor que 33    
4 pregunta -> número 3 es > 33 
    si> mostrar mensaje de que numero 3 es mayor que 33
    no> mostrar mensaje de que numero 3 no es mayor que 33

5 pregunta -> numero 1 es > que numero 2 
    si> preguntar si numero 1 es mayor que numero 3
        si> mostrar mensaje de que numero 1 es mayor
        no> pregunta -> si numero 2 es mayor que numero 3 
            si> mostrar mensaje ed que 2 es mayor
            no> mostrar mensaje de que 3 es mayor
    no> pregunta si numero 1 mayor que 3
        si> mostrar que 1 es mayor
        no> preguntar -> si numero 2 es mayor a numero 3
            si> mostrar que numero 2 es mayor
            no> mostrar que nuemro 3 es el mayor 

"""
"""
preguntar: si numero 1 > numero 2 y numero 1 > mayor 3
    si-- entonces numero 1 es mayor
    no-- preguntar: si numero 2 es mayor 3 
         si-- entonces numero 2 es mayor 
         no-- entonces numero 3 es mayor
"""