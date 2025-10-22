separador = "*" * 50 + "\n"
print(separador)

# Funcione
# -> str  indicamos que tipo va a devolver (str en este caso) o (nombre: str) de que tipo de dato recibe
def saludar(nombre: str) -> str:
    """ Funcion que devuelve un saludo """
    return f"Hola {nombre}"

print(saludar("Daniel"))

# Funcion con argumento por default
# Parametro por defecto e igual se puede pasar otro
def saludo_generico(nombre = "Usuario"):
    return f"Hola {nombre}"

print(saludo_generico("Arian"))

# Fyncion con argumento kwargs


# Funciones Lambda

def suma(num1: int, num2: int) -> int:
    # Suma de dos numeros
    return num1 + num2

suma_lambda = lambda n1, n2 : n1 + n2

print(suma(2, 3))
print(suma_lambda(2,3))

# Funciones Map y filter
""" Funcion que aplica a cada elemento de una lista una funcion"""

# Map
"""
Un map nos modifica cada elemento de mi lista
"""
lista_numeros = [1, 2, 3, 4 ,5]
set = {1, 2, 3} # Set no acepta duplicados

print("Antes de map y de filter")
print(lista_numeros)

""" Map recibe una funcion y una lista"""
tipo_dato = type(map(lambda x: x**2, lista_numeros))
print(f"Tipo de datos {tipo_dato}")

cuadrados = list(map(lambda x: x**2, lista_numeros))
cuadrados_set = list(map(lambda x: x**2, set))
print("Cuadrados con Map")
print(f"Lista: {cuadrados}")
print(f"Set: {cuadrados_set}")


# Filter 
"""
Un filter nos selecciona cada elemento de mi lista
"""
print("Pares con filter")
pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(pares)

print("Despues de map y de filter")
print(lista_numeros)
