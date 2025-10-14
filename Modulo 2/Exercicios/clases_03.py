class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str, email: str, saldo: float, limite: float, conta_ativa: bool, telefone: str, endereco: str, senha: int):
        self.nome = nome        
        self.idade = idade    
        self.__cpf = cpf                
        self.__email = email            
        self.__saldo = saldo              
        self.__limite = limite            
        self.__conta_ativa = conta_ativa  
        self._telefone = telefone        
        self._endereco = endereco        
        self._senha = senha
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def conta(self):
        return self.__conta_ativa
    
    @conta.setter
    def conta(self, valor):
        self.__conta_ativa = valor

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        self._senha = valor

    def despositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__log_transacao("Depósito", valor)
            print(f"Deposito de {valor} realizado")
            return True
        else:
            return False


    


    


    


    
    

 

     



    

