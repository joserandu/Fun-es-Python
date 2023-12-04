"""
FUNÇÕES COM RETORNO

A função deve ser isolada dentro do código com duas linhas de espaçamento em cima e em baixo.
"""

print('Relembrando ---------------------------------------------------------------------------------------------------')
numeros = [1, 2, 3]
ret = numeros.pop()
print(f'retorno de pop: {ret}')

ret_pr = print(numeros)
print(f'Retorno de ret_pr: {ret_pr}')  # Perceba que o código fica até redundante usando print() duas vezes.

"""
Repare que por conta de ret_pr não ser uma função de retorno, é impresso o valor None, pois não é dado nenhum valor 
resultante da função. A função não dá um retorno, ela dá uma impressão, entenda a diferênça.
"""

print('Exemplo de função ---------------------------------------------------------------------------------------------')

"""
ATENÇÃO: Agora que vamos estudar funções de retorno, necessita-se de uma mudança de vocabulário. O print não retorna 
valores, ele IMPRIME valores.
"""


def quadrado_de_7():
    print(7 * 7)


quadrado_de_7()

ret = quadrado_de_7()
print(f'Retorno: {ret}')

"""
Como essa última função não é uma função de retorno, esperar um valor de retorno dela é errado, pois não existe um 
valor de retorno, existe um valor de impressão. Portanto, o retorno é None.
"""

print('Refatorando a função de cima ----------------------------------------------------------------------------return')

# Refatorar significa redefinir/reescrever uma função.


def quadrado_de_6():
    return 6 * 6


retorno = quadrado_de_6()

print(f'Retorno: {retorno}')

"""
Criamos uma variável para receber o retorno da função e estamos imprimindo.
Repare que agora declaramos explicitamente que temos um valor/resultado para a função. 
Não precisamos necessáriamente para receber o retorno de uma função, podemos passar a execução da função para outras 
funções ou mesmo para outras funções.
"""

# Funções de retorno com contas
print(f'Retorno: {retorno + 1}')

print('Refatorando a função diz_oi -----------------------------------------------------------------------------------')


def diz_eai():
    return 'eai'  # Dessa forma, ao invés de imprimir, a função RETORNA.


print(diz_eai())
diz_eai()

"""
Se somente chamar a função, não será impresso nada, pois, no segundo caso não houve a instrução para impressão.
"""

print('Aplicação com junção de variáveis -----------------------------------------------------------------------------')


def diz_ola():
    return 'Olá, '


nome = 'Pedro'

print(diz_ola() + nome + '!')

"""
Se usassemos uma função sem retorno, na hora de concatenar a função com a(s) variável(is) e string(s) daria erro.

OBS: 
Sobre a palavra reservada RETURN

1 - Ela finaliza a função, ou seja, ela sai da execução da função.
2 - Podemos ter em uma função diferentes returns, mas ela só vai executar um.
3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores.
"""

print('Return como finalizador da função -----------------------------------------------------------------------------')


def say_my_name():
    print('Eu sou impresso')
    return 'Heiserberg'
    print('Eu não sou impresso')


print(say_my_name())

print('Usando if/elif/else -------------------------------------------------------------------------------------------')


def nova_funcao():
    variavel = False
    if variavel:  # is Truec
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())

"""
Eu poderia não ter escrito o else, mas eu ainda gosto dele e acho que ele deixa mais claro o código.
Tome cuidado com essas funções que as vezes por causa de besteira a gente acaba gastando muito tempo à toa.
Nessa função, caso você tenha esquecido tudo, só está passando um valor a variável e atribuindo a tomadas de decisões 
do if/else/elif.
"""

print('Utilizando uma Tupla na função de retorno -------------------------------------------------------return x, y, z')


def outra_funcao():
    return 2, 4, 6, 8


print(outra_funcao())
print(type(outra_funcao()))

print('Função para jogar uma moeda ----------------------------------------------from random import random // random()')

from random import random


def joga_moeda():
    valor = random()  # Gera um valor pseudo-randômico
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(f'A face que saiu na coroa é {joga_moeda()}')

"""
Para utilizar uma função randômica, precisamos importar a bibioteca ramdom. Mais pra frente, trabalharemos mais
profundamente sobre as bibliotecas.
"""

print('Refatorando o código ------------------------------------------------------------------------------------------')


def joga_moeda2():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(f'A face que saiu na coroa é {joga_moeda2()}')

"""
O random() é uma função, e ela não precisa ser igualada a uma variável. Economizamos uma linha de código.
Os valores de um random e outro dentro do código são independentes.
"""

print('Erros comuns na utilização do retorno -------------------------------------------')

"""
Não são erros própriamente ditos, mas sim, redundâncias o linhas que podem ser tiradas do código.
"""


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    #  else:
    return False


print(eh_impar())

"""
Na def acima, como já mostrado anteriormente, é recomendável não usar o else, pois não é necessário.
"""
