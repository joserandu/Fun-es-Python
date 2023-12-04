"""
FUNÇÕES COM PARÂMETROS (DE ENTRADA)
    *A redundância é para deixar bem claro isso:

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
"""

print('Função estática----------------')


def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())
print(quadrado_de_7())

"""
Essa função está estática e independentemente de quantas vezes imprimirmos ela o resultado sempre será o mesmo.
"""

print('Refatorando para deixar dinâmico ------------------------------===========--------def funcao(indicar_parâmetro)')


def quadrado(numero):  # Não se esqueça de indicar que a função espera um parâmetro.
    return numero * numero


print(quadrado(9))
print(quadrado(14))

"""
É no print() que colocamos o parâmetro da função.
"""

print('Usando operadores matemáticos -------------------------------------------------------------------------------**')


def quadrado2(numero):
    return numero ** 2


print(quadrado2(20))
print(quadrado2(18))

"""
Se não colocar um parâmetro quando indicamos que a função recebe parâmetros, o código acaba gerando erro.
"""

print('Refatorando a função cantar_parabens() --------------------------------------------------------(aniversariante)')


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Ra tim bum {aniversariante}, {aniversariante}, {aniversariante}')


cantar_parabens('Patrícia')

print('Funções com mais de um parâmetro ----------------------------------------------------------def funcao(x, y, z):')

"""
funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos parâmetros forem 
nessessários, sendo eles separados por vírgula (,).
"""


def soma(x, y):  # Esses são nossos parâmetros.
    return x + y


def multiplica(z, w):
    return z * w


def outra(a, b, c):
    return (a + b) * c


print(soma(25, 30))  # Esses são os nossos argumentos.
print(multiplica(7, 9))
print(outra(21, 2, 2))
print(outra(2, 3, 'Python '))  # Fazendo isso a string será repetida o número devido de vezes segundo os parâmetros.

"""
PARÂMETROS: É os espaços que abrimos na função para recebimento dos argumentos.
ARGUMENTOS: Dados enviados para a função.
Essa é a minha clara definição para quando eu ler eu entender, mas a definição mais formal é:

PARÂMETROS: Variáveis declaradas na definição de uma função;
ARGUMENTOS: Dados passados durante a execução de uma função;

Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError, seja com mais ou menos argumentos.
"""

print('Nomeando parâmentos -------------------------------------------------------------------------------------------')

"""
Em programação, sempre é importante que tudo faça sentido, para isso, precisamos saber nomear os parâmetros.
"""


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

"""
Lembre-se que a ordem dos argumentos importa.
"""

print('Argumentos nomeados --------------------------------------------------------------------------Keyword Arguments')

"""
Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
"""

print(nome_completo(sobrenome='José', nome='Randú'))

# OU
nome = 'Antonieta'
sobrenome = 'Maria'

print(nome_completo(sobrenome=nome, nome=sobrenome))

print('Erro comum na utilização de return ----------------------')


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

# Repare na diferênça entre os dois resultados:


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

"""
A diferênça na impressão dessas duas funções, que aparentemente são idênticas consistem na POSIÇÃO DO RETURN.
No segundo caso, pelo return estar na mesma casa que a estrutura do if, o código do if acaba acontecendo uma única vez, 
resultando em um único resultado (1). Já com o return mais recuado, como no primeiro caso, o loop será feito 
completamente para depois a finalização.

A função recebe qualquer tipo de parâmetro, pode ser tupla, lista, conteiner, string, dict, etc.
"""
