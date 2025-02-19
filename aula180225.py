# Função para calcular fatorial
def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

# Função para calcular combinações
def combinacao(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

# Função para calcular permutações
def permutacao(n, k):
    return fatorial(n) // fatorial(n - k)

# 1. Escalar um time de 6 jogadores a partir de 15 disponíveis
escalar_time = combinacao(15, 6)
print(f"Escalar time: {escalar_time} maneiras")

# 2. Vestir-se com 6 camisas e 4 calças
camisas = 6
calcas = 4
vestir = camisas * calcas
print(f"Vestir-se: {vestir} maneiras")

# 3. Sentar 6 amigos em um banco
sentar_amigos = fatorial(6)
print(f"Sentar amigos: {sentar_amigos} maneiras")

# 4. Formar o pódio em uma competição de xadrez com 8 jogadores
podio = permutacao(8, 3)
print(f"Formar pódio: {podio} maneiras")

# 5. Combos diferentes em uma lanchonete
sanduiches = 4
bebidas = 3
sobremesas = 2
combos = sanduiches * bebidas * sobremesas
print(f"Combos diferentes: {combos} maneiras")

# 6. Comissões de 4 elementos com 20 alunos
comissoes = combinacao(20, 4)
print(f"Comissões de 4 elementos: {comissoes} maneiras")

# 7. Anagramas da palavra FUNÇÃO
# a) Anagramas da palavra FUNÇÃO
anagramas_total = fatorial(7)  # 7 letras, sem repetição
print(f"Anagramas da palavra FUNÇÃO: {anagramas_total}")

# b) Anagramas que começam com F e terminam com O
anagramas_f_o = fatorial(5)  # 5 letras restantes
print(f"Anagramas que começam com F e terminam com O: {anagramas_f_o}")

# c) Anagramas onde A e O aparecem juntas
anagramas_ao_juntos = fatorial(6)  # 6 letras considerando "ÃO" como uma letra
print(f"Anagramas onde A e O aparecem juntas: {anagramas_ao_juntos}")

# 8. Organização da família de Carlos
familia = 5
organizacao_familia = fatorial(familia)
print(f"Organização da família: {organizacao_familia} maneiras")

# Carlos e Ana lado a lado
organizacao_carlos_ana = fatorial(4) * 2  # 4 unidades e 2 arranjos (CA ou AC)
print(f"Carlos e Ana lado a lado: {organizacao_carlos_ana} maneiras")

# 9. Comissões de 6 pessoas com 4 mulheres e 2 homens
comissoes_m = combinacao(6, 4) * combinacao(5, 2)
print(f"Comissões de 4 mulheres e 2 homens: {comissoes_m} maneiras")