# Percentual = (Faturamento p/ Estado / Faturamento total) * 100 -> o Cem é de porcentagem.

valores = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

totalValores = sum(valores.values())

for estado, faturamento in valores.items():
    percentual = (faturamento / totalValores) * 100
    print(f"{estado}: {percentual:.2f}%")