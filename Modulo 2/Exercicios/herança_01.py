class Personagem:
    def __init__(self, nome: str, idade: int, posicao: str, agilidade: int, forca: int, defesa: int, ger:int, lesao: bool, valor: float, clube: str, partidas: int):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.agilidade = agilidade
        self.forca = forca
        self.defesa = defesa
        self.ger = ger
        self.lesao = lesao
        self.valor = valor
        self.clube = clube
        self.partidas = partidas

    def jogar_partida(self):
        if self.lesao == True:
            return f"Jogador {self.nome} está machucado"
        else:
            return f"Jogador {self.nome} vem pra jogo"
        
    def jogador_estrela(self):
        if self.ger >= 89:
            return f"O {self.posicao} {self.nome}, é um dos melhores"
    
    def posse(self):
        if self.idade < 28:
            return f"O jovem {self.nome} com agilidade {self.agilidade} mantem a bola"
        else:
            return f"O experiente {self.nome} com força {self.forca} está com a posse"
        
    def trasnferencia(self):
        if self.valor > 5000000:
            return f"Este {self.posicao} é muito valioso"
        elif self.valor > 1000000:
            return f"O jogador {self.nome} custa caro"
        else:
            return f"{self.nome} tem um valor de transferencia normal"
        
    def time(self):
        return f"O profissional {self.nome} joga no clube {self.clube}"


        