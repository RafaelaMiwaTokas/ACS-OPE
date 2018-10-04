class ParametroNegativoException(Exception):
    pass

class ResultadoNegativoException(Exception):
    def __init__(self, resultado):
        self.resultado = resultado

class ParametroZeroException(Exception):
    pass

class OperacaoMuitoFacilException(Exception):
    def __init__(self, resultado):
        self.resultado = resultado