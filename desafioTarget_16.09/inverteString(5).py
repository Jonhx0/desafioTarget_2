stringPrincipal = input("Digite algo: ")
stringReversa = ''

for a in range(len(stringPrincipal) - 1, -1, -1):
    stringReversa += stringPrincipal[a]
    
print("Inversão: ", stringReversa)