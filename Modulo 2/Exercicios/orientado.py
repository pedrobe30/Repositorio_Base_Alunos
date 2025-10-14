class Passaro():
    
    def __init__(self, tamanho, cores, especie, sexo):
        self.tamanho = tamanho
        self.cores = cores
        self.especie = especie
        self.sexo = sexo

    def cantar(self):
        return print(f"Sou um {self.especie} cantando uma bela canção")
    
    def voar(self):
        return print('Batendo as asas e: voando...')
        
passaro1 = Passaro(0.14, ['Marrom', 'Branco', 'cinza'], 'Pardal', 'M')
passaro2 = Passaro(0.80, ['Cinza', 'Branco'], 'Pombo', 'F')
passaro1.cantar()
passaro2.cantar()