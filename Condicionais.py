# > Estruturas condicionais
idade = 18
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')

media = 10
presenca = 100
if media >= 7 and presenca >=70:
    print('Você foi aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')

#Exercicio

x = int(input("Digite um número inteiro: "))
if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x / 2 == 0:
    resp2 = "par"
else:
    resp2 = "impar"
print("O número {} é {} e {}.".format(x, resp1, resp2))

# Funções
animais = ['gato', 'coelho', 'macaco', 'girafa']
animais.função1('gato')
print(animais)
print(função2(animais))
print(animais.função3('coelho'))

 