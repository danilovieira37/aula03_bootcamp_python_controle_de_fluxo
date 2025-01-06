# 6. Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

# import re

# texto = "a raposa marrom, salta sobre o cachorro preguiçoso. A raposa é muito ligeira."

# #excluir_virgula_e_ponto = texto.replace(",","")
# excluir_virgula_e_ponto = re.sub(r'[.,"\'-?:!;]', '', texto)
# palavras = excluir_virgula_e_ponto.split()
# contagem_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)

# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [5, 20, 30, 45, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(n - minimo) / (maximo - minimo) for n in numeros]

# print(normalizados)

# 8. Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]
# usuarios_sem_email_valido = [usuario for usuario in usuarios if usuario["email"]=="" or usuario["nome"]==""]
# print(usuarios_sem_email_valido)

# 9. Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [34, 23, 76, 44, 45, 36, 2]
somente_pares = [pares for pares in numeros if pares % 2 == 0] 
print(somente_pares)
