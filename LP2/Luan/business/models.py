from business.exceptions import ParametroNegativoException, ResultadoNegativoException, OperacaoMuitoFacilException, ParametroZeroException
class Calculadora():
    def soma(self, a, b):
        if a < 0 or b < 0:
            raise ParametroNegativoException()
        return a + b

    def subtrai(self, a, b):
        if a < 0 or b < 0:
            raise ParametroNegativoException()
        resultado = a - b
        if resultado < 0:
            raise ResultadoNegativoException(resultado)
        return a - b

    def multiplica(self, a, b):
        if a == 1 or b == 1:
            raise OperacaoMuitoFacilException(a*b)
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise ParametroZeroException()