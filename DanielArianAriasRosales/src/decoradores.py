import time

"""Decorador funcion que envuelve otra funcion"""

# Utilidad de time
#print("Time ", time.time())
#sum([i**2 for i in range(100000)])
#print("Time ", time.time())

def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("Final")
    return envoltura

@decorador # Anotacion se debe poner en la funcion a decorar
def saludo():
    #print("Inicio")
    print("Hola mundo")
    #print("Final")

saludo()

#funcion_decorada = decorador(saludo)
#funcion_decorada()

# Generar un decorador que clacule el tiempo de ejecucuion de una funcion

def decorador_tiempo_calc(func):
    def wrapper():
        inicio = time.time()
        func()
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin - inicio} segundos")
    return wrapper

@decorador_tiempo_calc # Anotacion se debe poner en la funcion a decorar
def saludo():
    #print("Inicio")
    print("Hola mundo")
    time.sleep(2)
    #print("Final")

saludo()