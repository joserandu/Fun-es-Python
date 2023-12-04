"""
DEFININDO FUNÇÕES

É um dos pilares da programação em geral.
- Funções são pequenas partes de código que realizam tarefas específicas.
- Pode ou não receber entrada de dados e retornar uma saída de dados.
- Sâo muito úteis para executar procedimentos similares repetidas vezes.

OBS: Se você escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada.

Já utilizamos várias funções desde que inciamos o curso: print(), len(), max(), min(), count(), entre outras.
"""

print('Funções que suportam qualquer tipo de dado -----------------------------')

cores = ['verde', 'amarelo', 'azul', 'branca']
print(cores)  # imprime uma lista

curso = 'Programação em Python: Essencial'
print(curso)  # imprime uma string

# Repare que a função print() não liga para qual é o tipo de dado que é enviado para ele, somente executa.

print('Funções que não aceitam qualquer tipo de dado ------------------------------------')

# Eu comentei porque dá erro:
# curso.append('Mais dados ...')  # aqui retorna um AttributeError, pois o append não aceita acrescentar dados em uma
# string, apenas em algumas coleções.

cores.append('laranja')
print(cores)

print('Funções que não aceitam dados de entrada --------------------------------------------------------------.clear()')

cores.clear()  # veja que após o chamado da função nas opções de atalho aparece clear(self).
print(cores)

print('Origem dos métodos do Python ----------------------------------------------------------------------------------')
# Imagine que não houvesse esses métodos e a gente precisasse fazer do zero

print(help(print))  # Com essa função help(), a gente consegue entender mais ou menos como foi feito.

print('Princípio do DRY: Don`t Repeat Yourself (Não repita você mesmo) -----------------------------------------------')

"""
Também pode ser chamado de não repita o seu código, a ideia é que você não precise ficar repetindo linhas de código.
"""

print('Definindo funções ------------------------------------------------------------------------------------------def')

"""
Forma geral:
def nome_da_funcao(parâmetros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o implementamento da função acontece. 
Neste bloco, pode ter ou não retorno da função;

OBS: Veja que para definir uma função usamos a palavra 'def' informando ao Python que estamos definindo uma função. 
Também abrimos o bloco de código com o já conhecido dois pontos ':'
"""

print('')
print('Definindo a primeira função -----------------------------------------------------------------------------------')

# Definição
def diz_oi():
    print('oi!')

"""
OBS: 
1 - Veja que dentro das nossas funções podemos utilizar outras funções.
2 - Perceba que a nossa função só executa uma tarefa, ou seja, imprime 'oi'.
3 - Veja que essa função não recebe nenhum parâmetro de entrada. (O parâmentro de entrada pode ser uma variável)
4 - Essa função não retorna nada, pois ela só foi criada, mas não foi chamada.
"""

#Chamada de execução
diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar parênteses à frente do nome da função para executá-la.
"""

print('Mais um exemplo -----------------------------------------------------------------------------------------------')

def cantar_parabens():
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

cantar_parabens()
cantar_parabens()  # Essa função será executada o tanto de vez que a gente chamar.

print('Usando for in para facilitar a nossa vida ---------------------------------------------------------------------')

for n in range(2):
    cantar_parabens()

print('Igualando uma função à uma variável e chamando ----------------------------------------------------------------')

canta = cantar_parabens  # SEM PARÊNTESES
canta()

"""
Nâo é muito comum usar essa forma, mas fique com mais esse ensinamento.
"""
