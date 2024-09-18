import json

def lerFaturamento(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def calcularFaturamento(faturamentoData):
    contasValidas = [dia['valor'] for dia in faturamentoData if dia['valor'] > 0]
    
    contasMinimas = min(contasValidas) if contasValidas else None
    
    contasMaximas = max(contasValidas) if contasValidas else None
    
    mediaContas = sum(contasValidas) / len(contasValidas) if contasValidas else 0
    
    acimaMedia = sum(1 for value in contasValidas if value > mediaContas)   
    
    return {
        "contasMinimas": contasMinimas,
        "contasMaximas": contasMaximas,
        "mediaContas": mediaContas,
        "acimaMedia": acimaMedia
    }
    
file_path = 'faturamento.json'
faturamentoData = lerFaturamento(file_path)
    
calculo = calcularFaturamento(faturamentoData)
    
print(f"Menor valor de faturamento - {calculo['contasMinimas']}")
print(f"Maior valor do faturamento - {calculo['contasMaximas']}")
print(f"Média do faturamento - {calculo['mediaContas']:.2f}")
print(f"Dias superiores - {calculo['acimaMedia']}")
    