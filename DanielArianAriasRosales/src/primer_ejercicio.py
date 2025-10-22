"""
Simular el calculo del precio final de un producto con IVA aplicado
"""

# Funcion que devuelve precio con IVA aplicado
def precio_final(precio: int, iva: int):
    return (precio + (precio*iva)/100)

print(f"Precio final Funcion: {precio_final(100, 16)}")

# Funcion lamda que devuelve precio con IVA aplicado
precio_final_lambda = lambda precio1, iva1 : precio1 + ((precio1*iva1)/100)
print(f"Precio final Lambda {precio_final_lambda(150, 16)}")