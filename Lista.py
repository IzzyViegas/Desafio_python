# Com lista
notas = [7.9, 8.9, 10]

# Criando listas
"""lista = []
lista = list()
lista = [26, 'wallison', 3.14159, 'namorado']
listas_de_listas = [10, [16, 3, 1999]]"""

# Indexação e Slides (Fatiamento)
"""lista = ['Professor', 'Inteligente', 'Lindo', 'Walisson' ]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1])""" # último da lista

# Slides
"""lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lista[0:3])
print(lista[3:6])
print(lista[2:])
print(lista[2:6:2])"""

# 1. Utilizando os proprios elementos da lista
"""for elemento in lista:
    print(elemento)"""
# 2. Utilizando os índices
"""print('comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(i)"""

# Métodos de listas
lista = [ 1, 4, 6, 8, 9, 12]
print('Antes do append:', lista)

# append: adiciona elementos na lista
lista.append(14)
print('Depois do append:', lista)

# insert: escolhe a posição e adiciona
lista.insert(1, 2)
print('Depois do insert:', lista)

# extend : juntar duas listas jogando no final
lista2 = [16, 19, 20]
lista.extend(lista2)
print('Depois do extend:', lista)

# pop: remover o índice específico ou último
lista.pop(0)
print('Depois do pop:', lista)

# remove: remover o elemento
lista.remove(19)
print('Depois do remove:' , lista)

# count: contar números repetidos
print('Quantidade de 9 na lista:' , lista.count(9))

# index: diz o índice do elemento
print('Indice do elemento 12:' , lista.index(12))
# Sort: ordena lista
lista.sort(reverse=True)
print(lista)



