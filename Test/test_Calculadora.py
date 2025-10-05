import pytest
import Calculadora

def test_sumar():
    assert Calculadora.sumar (2,4) == 6

def test_dividir():
    assert Calculadora.dividir (100,2) == 50

def test_multiplicar():
    assert Calculadora.multiplicar (15,3) == 45

def test_restar():
    assert Calculadora.restar (85,10) == 75

def test_division_por_cero():
    with pytest.raises(ValueError):
         Calculadora.dividir(2,0)

@pytest.mark.parametrize("a,b,esperado",[ 
     (2,5,7),
     (-4,-2,-6),
     (0,0,0)
])
def test_sumar_varios(a,b,esperado):
    assert Calculadora.sumar(a,b) == esperado


def test_restar_con_fixture(numeros):
    a,b = numeros
    assert Calculadora.restar(a,b) == 0

def test_sumar_con_fixture(numeros):
    a,b = numeros
    assert Calculadora.sumar(a,b) == 10

@pytest.mark.listo
def test_sumar_listo():
    assert Calculadora.sumar(1,3) == 4

def test_estuructura_dicc():

    data = {"nombre": "Luisa", "Edad": 34}
    assert "nombre" in data
    assert isinstance(data["nombre"], str )

