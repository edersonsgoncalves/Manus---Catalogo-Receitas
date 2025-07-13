class Receita:
    def __init__(self, nome:str, ingredientes:list, modo_preparo:str):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo

    def __str__(self):
        itens = ""
        for item in self.ingredientes:
            itens += item+"\n"

        return f"-=-=\033[1m{self.nome}\033[0m=-=-\n\033[1m*Ingredientes*\033[0m\n{itens}\n\033[1m*Modo de Preparo*\033[0m\n{self.modo_preparo}"
    
    def valida_ingrediente (self, ingrediente):
        ingreditente_localizado = False
        for item in self.ingredientes:
            if ingrediente.lower() in item.lower():
                ingreditente_localizado = True
                return f"O item '{item}' foi localizado na receita."

        if not ingreditente_localizado:
            print (f"Não foram encontradas referencias ao ingrediente '{ingrediente}'")
            return
 