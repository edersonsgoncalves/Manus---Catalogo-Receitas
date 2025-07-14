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

catalogo_receitas = []

receita1 = Receita(
    nome="Panqueca",
    ingredientes=['1 xícara de farinha', '1 ovo', '1 xícara de leite', '1 pitada de sal'],
    modo_preparo="Misturar todos os ingredientes, bater até ficar homogêneo e fritar em frigideira antiaderente."
)
receita2 = Receita(
    nome="Brigadeiro",
    ingredientes=['1 lata de leite condensado', '2 colheres de sopa de chocolate em pó', '1 colher de sopa de manteiga'],
    modo_preparo="Misturar tudo em uma panela, levar ao fogo baixo mexendo até desgrudar do fundo. Enrolar bolinhas e passar no granulado."
)
receita3 = Receita(
    nome="Salada Caesar",
    ingredientes=['alface romana', 'croutons', 'queijo parmesão ralado', 'molho caesar'],
    modo_preparo="Lavar e rasgar as folhas de alface, misturar com croutons, regar com molho e finalizar com parmesão."
)
receita4 = Receita(
    nome="Macarrão Alho e Óleo",
    ingredientes=['500g de macarrão', '6 dentes de alho', '1/2 xícara de azeite', 'sal a gosto', 'pimenta dedo-de-moça'],
    modo_preparo="Cozinhar o macarrão. Refogar o alho no azeite até dourar, misturar com o macarrão escorrido e finalizar com pimenta."
)
catalogo_receitas.append(receita1)
catalogo_receitas.append(receita2)
catalogo_receitas.append(receita3)
catalogo_receitas.append(receita4)

for receita in catalogo_receitas:
    print (receita, "\n")