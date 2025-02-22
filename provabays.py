# Em uma prova de múltipla escolha, cada questão tem 5 alternativas, 
# sendo apenas uma delas correta.Ao não saber a resposta, 
# o aluno "chuta" aleatoriamente uma resposta qualquer entre as 
# possiveis escolhas. Levando-se em conta um ahmno mediaho, que 
# saiba 60% do conteúdo, qual será a chance de ele acertar uma 
# das 5 questões escolhida aleatoriamente? E qual a chance de ele 
# acertar exatamente 3 questões?

from math import comb

# Probabilidades
p_saber = 0.6            # Probabilidade de saber a resposta
p_chutar = 0.4           # Probabilidade de chutar (não sabe a resposta)

# Probabilidade de acertar uma única questão
p_acertar = p_saber + (p_chutar / 5)  # Probabilidade de acertar (sabe ou chuta certo)

print(f"Probabilidade de acertar uma questão: {p_acertar:.2f}")

# Calculando a probabilidade de acertar exatamente 3 questões em 5
n = 5  # número total de questões
k = 3  # número de acertos desejados

# Usando a fórmula da distribuição binomial
p_acertar_3 = comb(n, k) * (p_acertar ** k) * ((1 - p_acertar) ** (n - k))

print(f"Probabilidade de acertar exatamente 3 questões em 5: {p_acertar_3:.4f}")