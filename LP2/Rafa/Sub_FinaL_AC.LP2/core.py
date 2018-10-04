from business.models import Calculadora
from business.exceptions import ParametroNegativoException, ResultadoNegativoException, OperacaoMuitoFacilException, ParametroZeroException

op = 0
while op != 5:
    a = float(input("Insira o primeiro número: "))
    b = float(input("Insira o segundo número: "))
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    op = int(input("Escolha a operação desejada: "))
    if op == 1:
        print(Calculadora().soma(a,b))
       
    if op == 2:
        print(Calculadora().subtrai(a,b))

    if op == 3:
        print(Calculadora().multiplica(a,b))
       
    if op == 4:
        print(Calculadora().divide(a,b))


