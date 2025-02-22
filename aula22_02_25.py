from math import comb

# Função para calcular a probabilidade de sair um número ímpar
def probabilidade_impar_dado():
    numeros_impares = 3  # 1, 3, 5
    total_numeros = 6
    return numeros_impares / total_numeros

# Função para calcular a probabilidade de obter números iguais em dois dados
def probabilidade_numeros_iguais_dados():
    numeros_iguais = 6  # (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)
    total_combinacoes = 6 * 6
    return numeros_iguais / total_combinacoes

# Função para calcular a probabilidade de tirar uma bola azul
def probabilidade_bola_azul():
    bolas_azuis = 3
    total_bolas = 8
    return bolas_azuis / total_bolas

# Função para calcular a probabilidade de tirar um ás
def probabilidade_tirar_as():
    ases = 4
    total_cartas = 52
    return ases / total_cartas

# Função para calcular a probabilidade de escolher múltiplo de 2
def probabilidade_multiplo_de_dois():
    multiplos_de_dois = 10  # (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
    total_numeros = 20
    return multiplos_de_dois / total_numeros

# Função para calcular a probabilidade de obter "cara" 3 vezes ao lançar uma moeda 5 vezes
def probabilidade_cara_tres_vezes():
    n = 5  # total de lançamentos
    k = 3  # número de caras
    p = 0.5  # probabilidade de sair "cara"
    
    # Usando a fórmula da distribuição binomial
    prob = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return prob

# Funções para calcular as probabilidades de lançamentos de dados
def probabilidade_lancamentos_dados():
    # a) Probabilidade de obter 5 no primeiro e 4 no segundo
    prob_5_e_4 = (1/6) * (1/6)

    # b) Probabilidade de obter pelo menos um 5
    prob_n_5 = (5/6) * (5/6)  # Probabilidade de não obter 5 em nenhum dos lançamentos
    prob_pelo_menos_um_5 = 1 - prob_n_5

    # c) Probabilidade da soma dos lançamentos ser igual a 5
    combinacoes_soma_5 = 4  # (1,4), (2,3), (3,2), (4,1)
    total_combinacoes = 36
    prob_soma_5 = combinacoes_soma_5 / total_combinacoes

    # d) Probabilidade da soma dos lançamentos ser igual ou menor que 3
    combinacoes_soma_leq_3 = 3  # (1,1), (1,2), (2,1)
    prob_soma_leq_3 = combinacoes_soma_leq_3 / total_combinacoes

    return prob_5_e_4, prob_pelo_menos_um_5, prob_soma_5, prob_soma_leq_3

# Função para calcular a probabilidade de 3 meninos e 2 meninas
def probabilidade_meninos_e_meninas():
    n = 5  # total de filhos
    k = 3  # número de meninos
    p = 0.5  # probabilidade de ser menino
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Função para calcular a probabilidade de jogar futebol ou vôlei em um grupo de alunos
def probabilidade_futebol_ou_volei():
    alunos_futebol = 50
    alunos_volei = 40
    alunos_futebol_volei = 20
    total_alunos = 80
    
    p_futebol = alunos_futebol / total_alunos
    p_volei = alunos_volei / total_alunos
    p_futebol_e_volei = alunos_futebol_volei / total_alunos
    
    return p_futebol + p_volei - p_futebol_e_volei

# Função para calcular a probabilidade de sair número par ou primo
def probabilidade_par_ou_primo():
    pares = {2, 4, 6}
    primos = {2, 3, 5}
    numeros_validos = pares.union(primos)  # Unindo pares e primos
    total_numeros = 6  # 1, 2, 3, 4, 5, 6
    return len(numeros_validos) / total_numeros

# Executando as funções
print("Probabilidade de um número ímpar:", probabilidade_impar_dado())
print("Probabilidade de dois números iguais:", probabilidade_numeros_iguais_dados())
print("Probabilidade de tirar uma bola azul:", probabilidade_bola_azul())
print("Probabilidade de tirar um ás:", probabilidade_tirar_as())
print("Probabilidade de um número múltiplo de 2:", probabilidade_multiplo_de_dois())
print("Probabilidade de sair 'cara' 3 vezes:", probabilidade_cara_tres_vezes())
probs_lancamentos_dados = probabilidade_lancamentos_dados()
print("Probabilidade de 5 no primeiro e 4 no segundo:", probs_lancamentos_dados[0])
print("Probabilidade de pelo menos um 5:", probs_lancamentos_dados[1])
print("Probabilidade da soma ser 5:", probs_lancamentos_dados[2])
print("Probabilidade da soma ser igual ou menor que 3:", probs_lancamentos_dados[3])
print("Probabilidade de ter 3 meninos e 2 meninas:", probabilidade_meninos_e_meninas())
print("Probabilidade de jogar futebol ou vôlei:", probabilidade_futebol_ou_volei())
print("Probabilidade de sair número par ou primo:", probabilidade_par_ou_primo())