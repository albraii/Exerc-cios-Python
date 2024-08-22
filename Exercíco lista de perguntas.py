# Lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    respostas.append(resposta)

contador_sim = respostas.count("sim")

if contador_sim == 2:
    classificacao = "Suspeita"
elif 3 <= contador_sim <= 4:
    classificacao = "Cúmplice"
elif contador_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")
