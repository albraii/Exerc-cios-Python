temperaturas = []

while True:
    temp = input("Digite a temperatura (ou 'sair' para finalizar): ")
    if temp.lower() == 'sair':
        break
    try:
        temperaturas.append(float(temp))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número ou 'sair' para finalizar.")

if temperaturas: 
    menor_temp = min(temperaturas)
    maior_temp = max(temperaturas)
    media_temp = sum(temperaturas) / len(temperaturas)

    print(f"\nMenor temperatura: {menor_temp:.2f}°C")
    print(f"Maior temperatura: {maior_temp:.2f}°C")
    print(f"Média das temperaturas: {media_temp:.2f}°C")
else:
    print("Nenhuma temperatura foi informada.")
