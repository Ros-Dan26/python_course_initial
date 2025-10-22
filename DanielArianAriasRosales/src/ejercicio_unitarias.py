import requests

class Cliente:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo


    def validar_email(self) -> bool:
        """Valida la estructura de el correo"""
        return "@" in self.correo and "." in self.correo
    

   

client = Cliente("Daniel", "correo@axi.com")

print(client.validar_email())


# Ejemplo 3
class HttpClient:
    def __init__(self, url):
        self.url = url 

    def make_request(self, id):
        response = requests.get(f"{self.url}/{id}")
        return response.json()
    
http = HttpClient("https://rickandmortyapi.com/api/character")

print(http.make_request(10))





