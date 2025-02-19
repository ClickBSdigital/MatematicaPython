# 01= Quantas senhas com 4 algarismos diferentes podemos escrever com os algarismos 1, 2, 3, 4, 5, 6, 7, 8,e 9?

# Para calcular o número de senhas com 4 algarismos diferentes que podemos escrever com os algarismos 1, 2, 3, 4, 5, 6, 7, 8 e 9, podemos usar o conceito de permutação. Como a ordem dos algarismos importa e não podemos repetir algarismos, o número de possíveis senhas é dado por:

# [ P(9, 4) = \frac{9!}{(9-4)!} = 9 \times 8 \times 7 \times 6 ]

from math import perm
# Número de algarismos disponíveis
n = 9
# Número de algarismos na senha
k = 4
# Calculando o número de senhas possíveis
numero_de_senhas = perm(n, k)

print(f"O número de senhas possíveis é: {numero_de_senhas}")

# Número de algarismos disponíveis
n = 9

# Número de algarismos na senha
k = 4

# Calculando o número de senhas possíveis
numero_de_senhas = 1
i = 0
while i < k:
    numero_de_senhas *= (n - i)
    i += 1

print(f"O número de senhas possíveis é: {numero_de_senhas}")