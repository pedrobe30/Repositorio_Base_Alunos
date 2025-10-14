from herança_01 import Personagem

class Atacante(Personagem):
    def __init__(self, nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas, finalizacao: int):
        super().__init__(nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas)
        self.finalizacao = finalizacao
    
    def fazer_gol(self):
        if self.finalizacao > 80:
            return f"O Atacante {self.nome} fez um golaço"
        else:
            return f"Marca um gol o atacante {self.nome}"

class Meia(Personagem):
    def __init__(self, nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas, passe: int):
        super().__init__(nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas)
        self.passe = passe
    
    def visao_de_jogo(self):
        return f"O meia tem a visão de jogo aprimorada"
    
    def assistencia(self):
        if self.passe > 85:
            return f"{self.nome}, Meia, dá assistencias maravilhosas"
        elif self.passe < 65:
            return f"Apesar de jogar no meio de campo, ele não tem passes bons"
    
class Zagueiro(Personagem):
    def __init__(self, nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas):
        super().__init__(nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas)
    
    def estilo(self):
        if self.defesa > self.forca:
            return "Esse zagueiro tem mais tecnica"
        elif self.defesa < self.forca:
            return f"O zagueiro {self.nome} é mais forte"
        else:
            return f"{self.nome} é equilibrado"
    
    def marcar(self):
        if self.defesa > 84 and self.forca > 80 and self.agilidade > 75:
            return f"O {self.nome} é um dos melhores zagueiros atualmente"
        else:
            return f"É um bom zagueiro"
        
class Goleiro(Personagem):
    def __init__(self, nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas):
        super().__init__(nome, idade, posicao, agilidade, forca, defesa, ger, lesao, valor, clube, partidas)
    
    def defender_penalti(self, player):
        return f"O goleiro {self.nome} defendeu o penalti do jogador {player}"




atacante1 = Atacante(
    nome="Kaio Jorge", idade=25, posicao="Atacante", agilidade=87, forca=76,
    defesa=40, ger=90, lesao=False, valor=7500000, clube="Flamengo",
    partidas=120, finalizacao=92
)


meia1 = Meia(
    nome="Matheus Pereira", idade=29, posicao="Meia", agilidade=82, forca=70,
    defesa=60, ger=85, lesao=False, valor=4500000, clube="São Paulo",
    partidas=210, passe=88
)


zagueiro1 = Zagueiro(
    nome="Fabricio Bruno", idade=31, posicao="Zagueiro", agilidade=73, forca=85,
    defesa=88, ger=86, lesao=False, valor=3500000, clube="Palmeiras",
    partidas=180
)


goleiro1 = Goleiro(
    nome="Cassio", idade=34, posicao="Goleiro", agilidade=80, forca=78,
    defesa=90, ger=89, lesao=False, valor=2000000, clube="Corinthians",
    partidas=250
)



print(atacante1.jogar_partida())
print(atacante1.jogador_estrela())
print(atacante1.fazer_gol())
print(atacante1.time())
print(atacante1.trasnferencia())

print("------"*30)

print(meia1.assistencia())
print(meia1.visao_de_jogo())
print(meia1.posse())
print(meia1.trasnferencia())

print("------"*30)

print(zagueiro1.estilo())
print(zagueiro1.marcar())
print(zagueiro1.time())

print("------"*30)

print(goleiro1.defender_penalti("Yuri Alberto"))