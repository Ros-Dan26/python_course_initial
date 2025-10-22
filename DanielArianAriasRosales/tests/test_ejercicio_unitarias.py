from src.ejercicio_unitarias import Cliente

from src.ejercicio_unitarias import HttpClient

from unittest.mock import Mock

def test_validar_email_succes():
    #Arrange
    email_valido = "email@test.com"

    # Llamada
    cliente_test = Cliente("Daniel", email_valido)

    # Assert
    assert cliente_test.validar_email() is True 


def test_validar_email_fail():
    #Arrange
    email_valido = "emailtest.com"

    # Llamada
    cliente_test = Cliente("Daniel", email_valido)

    # Assert
    assert cliente_test.validar_email() is False


""" 
def test_make_request_success(monkeypatch):
    # arrange
    id = 20
    http_mock = Mock(status_code = 200)
    http_mock.json.return_value = {'some': 'data'}
    monkeypatch.setattr('requests.get', lambda url: http_mock)

    # act
    http_client = HttpClient('http://localhost:80/url/example.com')
    response = http_client.make_request(id)


    # assert
    assert response is not None
"""
