class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Empleado(Persona):
    def __init__(self, nombre, puesto):
        super().__init__(nombre)
        self.puesto = puesto

    def __str__(self):
        return f"Empleado {self.nombre} con puesto {self.puesto}"



empleado = Empleado("Daniel", "Trainee")

print(empleado)








