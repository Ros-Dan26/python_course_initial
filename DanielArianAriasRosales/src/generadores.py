# yield

def conteo_to_limit(limit: int):
    """ Contea desde 0 hasta limite"""
    print("Inicio de funcion tradicional: ")
    list = []
    for i in range(limit):
        print("En la posicion ", i ) #Preferible usar fstrings
        list.append(i)

    print("Finaliza la funcion tradicional ")
    return list


conteo_to_limit(10)

def conteo_gen(limit: int):
    """ Conteo desde 0 hasta limite"""
    print("Inicio del generador con yield: ")
    for i in range(limit):
        print("En la posicion", i)
        yield i
    print("Fin del generador")

print(type(conteo_gen(10)))
print(type(conteo_to_limit(10)))

for numero in conteo_gen(5):
    print("En generador ", numero)

for numero in conteo_to_limit(5):
    print("En tradicional ", numero)

""" Generador de serie de fibonacci

# fibonacci: Es la secuencia donde cada número es la suma de los dos anteriores
"""

