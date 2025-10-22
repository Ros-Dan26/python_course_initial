from src.dependencias.di_01 import RepositorioBD, ServicePedidos


def test_validar_dependencia():
    #Arrange
    repo = RepositorioBD()
    service = ServicePedidos(repo)
    pedido = "Taco"

    # Llamada
    service.crear_pedido(pedido)

    # Assert
    assert repo.guardar 