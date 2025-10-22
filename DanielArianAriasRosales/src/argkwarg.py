separador = "*" * 50 + "\n"
print(separador)

# args
# Argumentos posicionales
"""args es una tupla (inmutable)"""
def procesar_datos(*args) -> None:
    """ Recibe argumentos posicionales """
    print(f"Argumentos: {args}")


procesar_datos(10, 50, 5, 4, 2)


# Keyword arguments
def procesar_datos_kw(**kwargs) -> None:
    """ Recibe argumentos clave-valor """
    print(f"Argumentos: {kwargs}")

""" recibe un diccionario {clave, valor} o clave = valor"""
procesar_datos_kw(nombre = "Daniel", edad = 25)


