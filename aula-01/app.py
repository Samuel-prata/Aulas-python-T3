""" 
Esse é um comentário em bloco
você pode ignorar tudo aqui
É só para mostrar
"""

# tipo numerico inteiro = <class 'int'>
# idade_do_samuca = 23
# # tipo numerico real = <class 'float'>
# altura_do_samuca = 1.89
# # Tipo textual -> string = <class 'str'>
# mensagem = 'Você não deu o Olá, mundo para quebrar a maldição' 


# # print() -> Imprimir no console
# # type() -> Mostrar o tipo de dado inserido na variável
# print(type(idade_do_samuca))
# print(type(altura_do_samuca))
# print(type(mensagem))

# input() -> Receber os dados pelo console
# nome = input('Qual é o seu nome? ')

# print(f'Seja bem vindo {nome}') # fstring -> format string


numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

print(f'O resultado da soma é: {numero1 + numero2}')
print(f'O resultado da subtração é: {numero1 - numero2}')
print(f'O resultado da multiplicação é: {numero1 * numero2}')
print(f'O resultado da divisão é: {int(numero1 / numero2)}')
print(f'O resultado do resto da divisão é: {numero1 % numero2}')

