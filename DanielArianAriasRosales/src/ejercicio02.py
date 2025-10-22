# fibonacci: Es la secuencia donde cada número es la suma de los dos anteriores
"""
1 -> 2 -> 3 -> 5 -> 8 -> 13
"""

def serie_fib(limite: int):
    numero_anterior = 1
    numero_nuevo = 0
    for i in range(limite):
        numero_nuevo = numero_anterior + numero_nuevo
        yield (numero_nuevo)
        numero_anterior = numero_nuevo - numero_anterior
        
        
for numero_final in serie_fib(10):
    print(numero_final)