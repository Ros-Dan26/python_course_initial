from dataclasses import dataclass


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


### dataClass

@dataclass
class PersonaDto:
    nombre: str
    edad: int
    cat: str


person = PersonaDto("Arian", 25, "Trainee")

print(person)


