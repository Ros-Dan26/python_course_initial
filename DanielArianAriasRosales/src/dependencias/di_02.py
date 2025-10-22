from abc import ABC, abstractmethod
from dependency_injector import containers, providers

#Interfaz define comportamiento
class IRepositorioDB(ABC):
    @abstractmethod # Anotacion que indica que es abstracto
    def guardar(self, pedido):
        pass

# Implementacion de interfaz
class RepositorioDB(IRepositorioDB):
    def guardar(self, pedido):
        print(f"pedido {pedido} almacenado exitosamente")

class ApiTercerosAdapter(IRepositorioDB):
    def guardar(self, pedido):
        print(f"Guardado pero de forma distinta: {pedido}")

# Logica de negocio
class ServicePedido:
    def __init__(self, repositorio: IRepositorioDB):
        self.repo = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repo.guardar(pedido)
        print("Notificacion de almacenado")


# Dependency injector with pip
class Contenedor(containers.DeclarativeContainer):
    repositorio = providers.Singleton(RepositorioDB)
    service = providers.Factory(ServicePedido, repositorio=repositorio)
    


container = Contenedor()
service_instance = container.service()
service_instance_two = container.service()

service_instance.crear_pedido("Pan de muerto")
service_instance_two.crear_pedido("Pan de muerto")


print(service_instance_two is service_instance)












