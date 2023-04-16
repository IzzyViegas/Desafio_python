# WHILE
"""
numero_sorteado = 15
numero_escolhido = int(input('Informe um número de 1 a 20: '))
if numero_sorteado == numero_escolhido:
    print('Você acertou!')
else:
    print('Você errou!')

numero_sorteado = 16
numero_escolhido = int(input('Informe um número de 1 a 20: '))
while numero_sorteado != numero_escolhido:
    print('Você errou, tente novamente!')
    numero_escolhido = int(input('Informe um número de 1 a 20: '))
"""
# Exemplo 2: Estrutura com contador
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1

# WHILE
cont = 0
resultado = 0
n = 1000

while cont != n:
    resultado = resultado + 1/(2**cont)
    cont = cont + 1
print(resultado)