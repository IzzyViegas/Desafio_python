# Exercicios de Python

# RESPOSTA NEGATIVA
x = 4.2
y = 10
z = "42"
print(not(((x * y == z) and not (x < y)) or y % 2 == 0))

# Qual é a resposta?
print(not(x < y and x * y == z)) or (x >= y or y % 2 == 0)
print(not((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z))))))
print(not(((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))))

# PAR OU IMPAR
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:
  resposta = a % 2 == 0
elif b > a and b > c:
  resposta = b % 2 == 0
else:
  resposta = c % 2 == 0
print('O maior número entre os três informados é par?', resposta)
(3,5,1), (1,5,2), (4,1,9), (4,5,9), (6,8,2), (9,9,11),(6,7,9)

# OPERADORES LÓGICOS
x = 10
y = 4.2
num = float(input("Digite um número a seguir: "))
print(num > x*y, num <= x + y, num*y != x*y)
print(num == x*y, num*y == x*y, y > x + num)

