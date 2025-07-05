import pytest
from src.calculadora.Operaciones.raiz_cuadrada import raiz_cuadrada

def datos_test_unit():
    return [
        25, 5
    ]

@pytest.mark.parametrize(
    "num, esperado", datos_test_unit()
)
def test_raiz_cuadrada(num, esperado):
    assert(
        raiz_cuadrada(num) == esperado
    )
