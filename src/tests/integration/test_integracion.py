import pytest
from src.calculadora.Operaciones.raiz_cuadrada import raiz_cuadrada
from src.calculadora.Operaciones.sumar import sumar

def datos_test_integracion(sum_a, sum_b):
    return [
        (10, 10, 3, 2, 5)
    ]

@pytest.mark.parametrize(
    "sum_a, sum_b, sum_c, sum_d, esperado", datos_test_integracion()
)
def test_sum_then_sqrt(sum_a, sum_b, sum_c, sum_d, esperado):
    assert(
        total = sumar(sum_a, sum_b, sum_c, sum_d)
        raiz_cuadrada(total) == esperado
    )
