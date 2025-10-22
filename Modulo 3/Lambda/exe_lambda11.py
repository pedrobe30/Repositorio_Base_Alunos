numbers = [-4.4, 54, -1.7, 12, 1.2, 0.50, 0.75, 8, 210, -10]

resto = lambda z: z%2 == 0
resultado_resto = list(map(resto, numbers))

print(resultado_resto)