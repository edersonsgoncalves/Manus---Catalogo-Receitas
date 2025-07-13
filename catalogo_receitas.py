class Receita:
    def __init__(self, nome:str, ingredientes:list, modo_preparo:str):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo

    def __str__(self):
        return f"\033[1m{self.nome}\033[0m\n\n*Ingredientes\n{self.ingredientes}\n\n*Modo de Preparo\n{self.modo_preparo}"
    
    def valida_ingrediente (self, ingrediente):
        self.ingrediente = ingrediente
        
        for item in self.ingredientes:
            if self.ingrediente.lower() == item.lower():
                return True