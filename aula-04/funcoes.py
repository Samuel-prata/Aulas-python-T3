'''FUNÇÕES'''

'''
- FUNÇÕES SEM PARAMETROS E SEM RETORNO
- FUNÇÕES COM PARAMETROS E SEM RETORNO
- FUNÇÕES SEM PARAMETROS E COM RETORNO
- FUNÇÕES COM PARAMETROS E COM RETORNO
'''

# criando a função sem parametros e sem retorno
print('SAIDA DA FUNÇÃO SEM PARAMETROS E SEM RETORNO')
def somar_dois_numeros():
    numero1 = 10
    numero2 = 10
    
    print(numero1 + numero2)
    
somar_dois_numeros()

print('-'*100)
print('SAIDA DA FUNÇÃO COM PARAMETROS E SEM RETORNO')

# Criando a função com parametro e sem retorno
def somar_dois_numeros(numero1: int, numero2: int):
    print(numero1 + numero2)

somar_dois_numeros(10,20)

print('-'*100)
print('SAIDA DA FUNÇÃO SEM PARAMETROS E COM RETORNO')
#Criando a função sem parametro e com retorno
def somar_dois_numeros():
    numero1 = 100
    numero2 = 1000
    return numero1 + numero2

resultado = somar_dois_numeros()
print(resultado)

print('-'*100)
print('SAIDA DA FUNÇÃO COM PARAMETROS E COM RETORNO')

#Criando a função com parametro e com retorno
def dividir_dois_numeros(numero1, numero2):
    return numero1 / numero2

resultado = dividir_dois_numeros(10,5)

print(resultado)

print('-'*100)

# *args -> Recebe uma tupla como argumento.
# Essa função pode receber vários argumentos
def somar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

resultado = somar(1,5,2,8,7,4,6,2,5,5,1,9,100,1854,1654159,8,15489,15489,6489,654, 18748798749, 654194)

print(resultado)
    