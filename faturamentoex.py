import json

with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)['faturamento']



    faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    menor = min(faturamento)
    maior = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima = len([dia for dia in faturamento if dia > media_mensal])
 

print(f"Menor valor: R${menor}")
print(f"Maior valor: R${maior}")
print(f"Dias acima da média: {dias_acima}")
