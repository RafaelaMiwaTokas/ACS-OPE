import pytest
from business.models import Calculadora

def test_soma():
    assert Calculadora().soma(1, 1) == 2

def test_subtracao():
    assert Calculadora().subtrai(1, 1) == 0

def test_multiplicacao():
    assert Calculadora().multiplica(10, 2) == 20

def test_divisao():
    assert Calculadora().divide(10,2) == 5


    
        