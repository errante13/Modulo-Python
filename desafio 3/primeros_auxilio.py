print("--------- primeros auxilios -------")
respuesta = input("La persona responde a estimulos, Favor responder si o no\n?").lower()
if respuesta=="si":
    print("evalue la necesidad de llevarlo al hospital más cercano\n")
else:
    print("Abra la via aerea de la persona\n")

    respuesta=input("la persona respira?, usar si o no\n").lower()
    if respuesta =="si":
        print("coloque a la persona en una posición de suficiente ventilación\n")
    else:
        print("administrar 5 ventilaciones y llame a la ambulancia\n")
        ambulancia = False
        while ambulancia == False:
            signos_vida=input("tiene signos de vida?? \n").lower()
            if signos_vida =="si":
                print ("reevaluar a la espera de la ambulancia\n")
            else:
                print ("vuelva aplicar compresiones\n") 
                
            respuesta=input("llegó la ambulancia, favor usar si o no\n").lower()
            if respuesta=="si":
                    ambulancia=True
                
print("----- fin Primeros auxilios -----")