''' DICIONARIOS '''


'''
- CHAVE: VALOR
- A CHAVE É UNICA E IMUTAVEL 
- DECLARAÇÃO -> {}
'''

# declaramos o nosso dicionario
dados_pessoais = {'nome_completo': 'Kleber Matos', 'cpf': '178.956247-93', 'email': 'Klebinprefeito@gmail.com'}

print(dados_pessoais)

print('-'*100)

print(dados_pessoais['nome_completo'])

# dados_pessoais['Nome_completo'] = 'Xaropinho do Ratinho'

print(f'o nome passou a ser {dados_pessoais['nome_completo']}')

print('-'*100)
print(dados_pessoais)

print('-'*100)

# get() -> Procura a chave e retorna uma mensagem padrão caso a mesma não tenha sido encontrada
print(dados_pessoais.get('nome_completo', 'Essa chave não existe no dicionário'))
print('Essa linha foi impressa após o get')

print('-'*100)

# keys() -> Retorna as chaves presentes
print(f'As chave do dicionário são: {dados_pessoais.keys()}')
# values() -> Retorna os valores presentes
print(f'Os valores do dicionário são: {dados_pessoais.values()}')

print('-'*100)

#Dicionario com dados atualizados
atualizacao = {'profissao': ['Empresario', 'Desenvolvedor', 'Instrutor', 'Prefeito', 'Presidente', 'Designer'], 'idade': 18, 'nome_completo': 'Kleber Matos de Souza', 'spa': 2134123948, 'mst': 'j12h481735$!#@412'}

# Atualiza o dicionario dados pessoais com os dados do dicionario atualizacao
dados_pessoais.update(atualizacao)

print(dados_pessoais)

print('-'*100)

# Deleção da chave e do valor com o del
del dados_pessoais['spa']
# Deleção com o pop() -> o método retorna o valor que foi 
print(dados_pessoais.pop('mst'))

print(dados_pessoais)

print('-'*100)

for chave, valor in dados_pessoais.items():
    print(f'A chavalore {chave} está associada ao valor {valor}')
