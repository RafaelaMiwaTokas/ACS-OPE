import pytest
from business.models import Calculadora
from business.exceptions import ParametroNegativoException,ResultadoNegativoException, OperacaoMuitoFacilException, ParametroZeroException
#Para rodar os testes, clique Ctrl+, e 
# copie e cole este comando abaixo comentado  V

#{
#  "python.unitTest.unittestEnabled": false,
# "python.unitTest.pyTestEnabled": true,
#  "python.unitTest.nosetestsEnabled": false,
#}

# em USER SETTINGS

def test_soma():
    assert Calculadora().soma(12,3)==15

    with pytest.raises(ParametroNegativoException):
        Calculadora().soma(12,-3)

def test_subtrai():
    assert Calculadora().subtrai(12,1)==11

    with pytest.raises(ParametroNegativoException):
        Calculadora().subtrai(2,-34)
    with pytest.raises(ResultadoNegativoException):
        Calculadora().subtrai(1,68)

def test_divide():
    assert Calculadora().divide(12,1)==12

    with pytest.raises(ParametroZeroException):
        Calculadora().divide(1,0)

def test_multiplica():
    assert Calculadora().multiplica(2,3)==6

    with pytest.raises(OperacaoMuitoFacilException):
        Calculadora().multiplica(12,1)
        