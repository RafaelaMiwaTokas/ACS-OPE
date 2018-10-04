''' 
'' 1. Separe seu projeto em diretorios:
''    - core.py (execucao do codigo principal do projeto)
''    + tests
''      - tests.py
''    + business
''      - models.py
''      - exceptions.py
''
'' 2. Evolua a calculadora para que ela tenha
''    os seguintes comportamentos:
''    + Soma:
''      Não deverão ser permitidos parametros
''      negativos, se acontecer devera ser 
''      lancada a excecao ParametroNegativoException
''
''    + Subtracao:
''      Não deverão ser permitidos parametros
''      negativos, se acontecer devera ser 
''      lancada a excecao ParametroNegativoException
''      O resultado de uma subtracao negativa deve
''      lancar uma excecao ResultadoNegativoException
''      e nesta excecao devera haver um atributo
''      chamado resultado com o valor resultante
''
''    + Divisao:
''      Divisao por zero nao deve lancar ZeroDivisionError,
''      e esperada uma excecao ParametroZeroException
''
''    + Multiplicacao:
''      Multiplicacoes onde qualquer um dos
''      parametros seja 1 devera retornar
''      OperacaoMuitoFacilException contendo um 
''      atributo resultado com o valor resultante
''
''  3. Crie todos os testes que garantam o comportamento
''     esperado
''
''  4. Crie um aplicativo de linha de comando (core.py)
''     na raiz do projeto para utilizar os modulos criados
''     e utilizar as funcionalidades previstas interagindo
''     com o usuario
'''