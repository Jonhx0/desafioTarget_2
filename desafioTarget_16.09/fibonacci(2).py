# Guarda um número usando input() e verifica se é inteiro com o int() na variável 'numero'.
numero = int(input("Digite um número: "))

# Valores inicias de Fibonacci.
a, b = 0, 1

# Loop para avançar a sequência.
while b < numero:
    a, b = b, a + b
    
# Verificação do número em relação à sequência.
if b == numero or numero == 0:
    print(f"O número {numero} está na sequência de Fibonacci.")
else:
    print(f"O número {numero} não está na sequência de Fibonacci.")