class Producto:
    """ Clase producto. Propiedades de un producto. """

    def __init__(self, nombre: str, precio: float):
        """ Constructor de clase """
        self.nombre = nombre
        self.precio = precio

producto_uno = Producto("Pan integral", 30.5)

print(f"Producto 1: {producto_uno.nombre} costo {producto_uno.precio} ")

# Property y setter


class ProductoSetter:
    """ Clase producto. Propiedades de un producto. """

    def __init__(self, nombre: str, precio: float):
        """ Constructor de clase """
        self.nombre = nombre
        self.precio = precio

    @property # Anotacion que permite protefer la propiedad (solo para obtener el valor)
    def precio(self) -> float:
        """ Getter, Nos permite acceder a la propiedad de .precio pero sin pasarle los parentecis"""
        return self._precio
    

    @precio.setter
    def precio(self, value: float):
        """ Nos permite modificar el valor de la propiedad y aplicar validacion """
        if value <= 0:
            raise ValueError("Ek precio debe ser mayor a 0")
        self._precio = value


    def __str__(self) -> str:
        """Metodo especial que nos permite el llamado para convertir a cadena de texto """
        return f"El producto {self.nombre} tiene un costo de {self.precio}"




producto_dos = ProductoSetter("Pan de Linaza", 32.5)
print(producto_dos)
print(f"Producto 2: {producto_dos.nombre} costo {producto_dos.precio} ")

producto_dos.precio = 45.2
print(f"Producto 2: {producto_dos.nombre} costo {producto_dos.precio} ")




