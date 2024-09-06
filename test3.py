# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
#que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('test3.json') as file:
    data = json.load(file)

faturamentoDiario = data["faturamento_diario"]

menorValor = 0
maiorValor = 0
somaValores = 0
diasFaturamento = 0

for dia in faturamentoDiario:
    valor = dia["valor"]
    if valor > 0:
        if valor < menorValor:
            menorValor = valor
        if valor > maiorValor:
            maiorValor = valor
        somaValores += valor
        diasFaturamento += 1

mediaMensal = somaValores / diasFaturamento

acimaDaMedia = sum(1 for dia in faturamentoDiario if dia["valor"] > mediaMensal)

print(f"Menor valor de faturamento: R$ {menorValor}")
print(f"Maior valor de faturamento: R$ {maiorValor}")
print(f"Número de dias com faturamento acima da media: {acimaDaMedia}")