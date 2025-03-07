'''SISTEMA DE CADASTRO COM ARMAZENAMENTO EM CSV'''

import csv # manipulação de arquivos csv
import time # Timer
import os # manipula o sistema operacional


print('-'*70)
nome_completo = input('Digite seu nome completo: ').lower()
print('-'*70)
data_de_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
print('-'*70)
cpf = input('Digite seu CPF (111.222.333-44): ')
print('-'*70)
email = input('Digite seu email: ').lower()
print('-'*70)
numero_do_cartao_de_credito = input('Digite o número do seu cartão: ')
print('-'*70)


with open('ficha_cadastro.csv', 'a') as arquivo: # a -> Append = Acrescentar
    escritor = csv.writer(arquivo) # Escritor tem todas as funções para manipular o arquivo CSV
    escritor.writerow([nome_completo, data_de_nascimento, cpf, email, numero_do_cartao_de_credito]) #Pegando um array com as informações e enviando para o arquivo
    # Cada array adicionar uma linha de informação

os.system('cls')
print('***********************************')
print('* Cadastro realizado com sucesso! *')
print('***********************************')

time.sleep(3)

os.system('cls')

for i in range(0,10):
    print(f'Gerando o arquivo em {i+1}')
    time.sleep(1) # Delay de 1 segundo
    os.system('cls') # roda no terminal o comando para limpar o terminal

with open('ficha_cadastro.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    for linha in dados:
        print(linha)
