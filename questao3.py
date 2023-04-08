import json

# abre o arquivo faturamento.json e carrega seu conteúdo na variável faturamento
with open('dados.json') as file:
    faturamento = json.load(file)

# Inicializando as variáveis do menor e maior faturamento com um valor alto e baixo, respectivamente
menor_faturamento = float('inf')
maior_faturamento = float('-inf')

# Calculando a soma dos valores de faturamento
soma_faturamento = 0
for dia in faturamento:
    if dia['valor'] != 0:
        soma_faturamento += dia['valor']

        # atualizando as variáveis do menor e maior faturamento se o valor atual for menor ou maior que o valor salvo
        if dia['valor'] < menor_faturamento:
            menor_faturamento = dia['valor']
        if dia['valor'] > maior_faturamento:
            maior_faturamento = dia['valor']

# calculando a média de faturamento
dias_com_faturamento = len([dia for dia in faturamento if dia['valor'] != 0])
media_faturamento = soma_faturamento / dias_com_faturamento

# contando quantos dias tiveram valor de faturamento acima da média mensal
dias_acima_media = 0
for dia in faturamento:
    if dia['valor'] > media_faturamento:
        dias_acima_media += 1

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"{dias_acima_media} dias tiveram faturamento acima da média mensal de R${media_faturamento:.2f}.")
