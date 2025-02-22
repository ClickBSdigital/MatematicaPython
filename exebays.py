# Em um teste de covide que o teste deu 90%. 
# faca o calculo em teorema de bays

# Para aplicar o Teorema de Bayes a um teste de COVID-19 com uma taxa de acerto de 90%, precisamos considerar as seguintes definições:

# P(C|+): Probabilidade de ter COVID-19 dado que o teste deu positivo.
# P(+|C): Probabilidade de testar positivo dado que se tem COVID-19 (sensibilidade do teste): 90% = 0.9.
# P(+|¬C): Probabilidade de testar positivo dado que não se tem COVID-19 (falsos positivos). Vamos assumir que essa taxa é 5% = 0.05 (ajuste conforme necessário).
# P(C): Probabilidade de realmente ter a COVID-19 na população. Vamos assumir, por exemplo, 1% = 0.01 (ajuste conforme necessário).
# Agora, o Teorema de Bayes é definido como:

# [ P(C|+) = \frac{P(+|C) \cdot P(C)}{P(+)} ]

# onde:

# [ P(+) = P(+|C) \cdot P(C) + P(+|¬C) \cdot P(¬C) ]

# Definindo as probabilidades
P_C = 0.01      # Probabilidade de ter COVID-19
P_negC = 1 - P_C  # Probabilidade de não ter COVID-19
P_pos_given_C = 0.9  # Sensibilidade do teste
P_pos_given_negC = 0.05  # Taxa de falso positivo

# Calculando P(+)
P_pos = (P_pos_given_C * P_C) + (P_pos_given_negC * P_negC)

# Calculando P(C|+)
P_C_given_pos = (P_pos_given_C * P_C) / P_pos

print(f'A probabilidade de ter COVID-19 dado que o teste deu positivo é: {P_C_given_pos:.4f}')