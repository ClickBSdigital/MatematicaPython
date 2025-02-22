# Numa certa região, a probabilidade de chuva em um dia qualquer de primavera é de 0,1. Um
# meteorologista da TV acerta suas previsões em 80% dos dias em que chove e em 90% dos dias em que
# não chove.
# a. Qual é a probabilidade do meteorologista acertar sua previsão?
# b. Se houve acerto na previsão feita. qual a probabilidade de ter sido um dia de
# chuva?

# Definindo as probabilidades
P_chuva = 0.1           # P(A): Probabilidade de chuva
P_acerto_chuva = 0.8    # P(B|A): Probabilidade de acerto se chover
P_acerto_sem_chuva = 0.9 # P(B|A'): Probabilidade de acerto se não chover

# Calculando a probabilidade do meteorologista acertar
P_nao_chuva = 1 - P_chuva          # P(A'): Probabilidade de não chover
P_acerto = (P_acerto_chuva * P_chuva) + (P_acerto_sem_chuva * P_nao_chuva) # P(B)

# Calculando a probabilidade de ter sido um dia de chuva dado que houve acerto
P_chuva_dado_acerto = (P_acerto_chuva * P_chuva) / P_acerto   # P(A|B)

# Imprimindo os resultados
print(f"Probabilidade do meteorologista acertar a previsão: {P_acerto:.4f}")
print(f"Probabilidade de ter sido um dia de chuva dado que houve acerto: {P_chuva_dado_acerto:.4f}")