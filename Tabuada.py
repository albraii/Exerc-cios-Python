numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if inicio > fim:
    print(f"tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim - 1, -1):
        print(f"{numero} x {i} = {numero * i}")
else:
    print(f"tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")
