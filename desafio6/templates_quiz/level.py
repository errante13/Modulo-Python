def choose_level(n_pregunta, p_level):
    nivel ="" 
    if n_pregunta <= p_level:
        nivel="basicas"
    elif n_pregunta <= 2*p_level:
        nivel="intermedias"
    else:
        nivel ="avanzadas"
    return nivel

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias