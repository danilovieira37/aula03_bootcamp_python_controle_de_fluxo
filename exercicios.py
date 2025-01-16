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

# numeros = [34, 23, 76, 44, 45, 36, 2]
# somente_pares = [pares for pares in numeros if pares % 2 == 0] 
# print(somente_pares)

# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)

# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# dados = []
# entrada = ''
# while entrada.lower() != 'sair':
#     entrada = input('Digite algum dado (ou sair para fechar a aplicação): ')
#     if entrada.lower() != 'sair':
#         dados.append(entrada)

# print(dados)

# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = int(input('Digite um número de 1 a 10: '))
# while numero < 1 or numero > 10:
#     print('Número fora do intervalo informado!')
#     numero = int(input('Número inválido, por favor digite um número de 1 a 10: '))

# print('Número válido')

# 13. Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
paginas_totais = 2 # Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f'Processando página {pagina_atual} de {paginas_totais}.')
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print('Processamento concluído')
