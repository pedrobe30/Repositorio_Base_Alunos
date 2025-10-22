cubo = lambda x: x**3

print(cubo(3))

delta = lambda a, b, c: (b**2) - 4*a*c
print(delta(1, 12, -13))

baskhara1 = lambda delta, b, a: -b + (delta**0.5) / 2 * a
baskhara2 = lambda delta, b, a: -b - (delta**0.5) / 2 * a

numeros = [1, 2, 3 ,4 ,5, 6]
quadrado = lambda x: x * x
quadrados = list(map(quadrado, numeros))

print(quadrados)

nomes = ["Boa", "Luffy", "Zoey", "Rumi", "Seong Gi-hun", "Léo", "Fábio", "Dedé", "Souza", "Goulart" ]
nomes_longos = list(filter(lambda nome: len(nome) > 4, nomes))

print(nomes_longos)

jogadores = [
    {'nome': 'Luansovisk', 'score': 2920, 'level': 17},
    {'nome': 'bernardino', 'score': 5260, 'level': 20},
    {'nome': 'AfonsoMilgrau', 'score': 3011, 'level': 12},
    {'nome': 'SamuelSPFC', 'score': 7621, 'level': 21},
    {'nome': 'DagobertoAless01', 'score': 15000, 'level': 99},
]

ranking = sorted(jogadores, key=lambda joagador: joagador['score'], reverse=True)
print("Jogadores com mais pontos:")
for jogador in ranking:
    print(jogador['nome'], jogador['score'])
