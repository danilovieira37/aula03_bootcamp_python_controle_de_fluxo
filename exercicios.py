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

numeros = [5, 20, 30, 45, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(n - minimo) / (maximo - minimo) for n in numeros]

print(normalizados)