''' LISTAS '''

'''
- PERMITE DUPLICATAS
- ESTRUTURA DE DADOS ORDENADA
- [ STRINGS, NUMEROS INTEIROS, NUMEROS REAIS, BOOLEANOS]
'''

# SEMPRE QUE APARECER DADOS DENTRO DE UM COLCHETO, TEREMOS UMA LISTA
lista_de_filmes = ['a procura da felicidade', 'Interestellar', 'Escritores da liberdade', 'Tarzan', 'Rei Leão', 'Hitch o conselheiro amoroso', 'Matrix', 'Procurando nemo', 'O som do coração', 'O Universo no Olhar', 'Karynight', 'O menino do Pijama Listrado']

print(lista_de_filmes)
print('-' *100)

# Append() - > Adiciona elementos no final da lista
lista_de_filmes.append('As tranças do rei careca')

print(lista_de_filmes)
print('-' *100)

# insert() -> adiciona no indice desejado
lista_de_filmes.insert(10, 'Spirit: O corcél indomavel')
print(len(lista_de_filmes))
print(lista_de_filmes)

print('-' *100)
lista_de_filmes.append('Hitch o conselheiro amoroso')

print(lista_de_filmes)

print('-'*100)

# pop() sem parametros - Exclui o ultimo elemento da lista
# pop(indice) - remove o elemento no indice indicado
lista_de_filmes.pop(3)
print(lista_de_filmes)

print('-'*100)

# index() -> Encontra a posição do elemento 
print(lista_de_filmes.index('Escritores da liberdade'))

print('-'*100)
lista_de_filmes.append('Hitch o conselheiro amoroso')

# count() -> Conta quantos vezes o mesmo elemento aparece na lista
print(f'O elemento aparece {lista_de_filmes.count('Hitch o conselheiro amoroso')} vezes')

print('-'*100)

# sort() -> ordena a lista
lista_de_filmes.sort()

# chama o elemento pelo indice
print(lista_de_filmes[0])
