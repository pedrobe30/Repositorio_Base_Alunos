class AnimaisMarinhos():

    def __init__(self, especie, habitat, tamanho, sexo,  nada, branquias):
        
        self.especie = especie
        self.habitat = habitat
        self.tamanho = tamanho
        self.sexo = sexo
        self.nada = nada
        self.branquias = branquias
    
    def nadar(self):
        if 'Sim' in self.nada:
            return print(f"Olá sou um {self.especie} e consigo Nadar")
        else:
            return print(f"Olá sou um {self.especie} e não consigo Nadar")
    
    def respirar_dentro_agua(self):
        if self.branquias == True:
            return print(f"{self.especie} conseguem respirar debaixo de água")
        else:
            return print(f"{self.especie} não consegue respirar debaixo da água")
    
    def alimentacao(self):
        return print(f" Me chamo {self.especie} e me alimento da cadeia marinha")
    
    def agua(self):
        return print(f"Dependo da Água para sobreviver")
    
    @staticmethod
    def machoFemea():
       sexo =  input("Está cadastrando um Macho ou Femea: ")
       sexo_refatorado = sexo.lower()

       if 'femea' in sexo_refatorado or 'f' in sexo_refatorado:
           return 'femea'
       
       elif 'macho' in sexo_refatorado or 'm' in sexo_refatorado:
           return 'macho'
       
       else:
           print ("Tente Novamente")
           return AnimaisMarinhos.machoFemea()





        

    


        