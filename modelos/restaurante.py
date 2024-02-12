class Restaurante:
    def __init__(self, nome, categoria) -> None:
       self.nome = nome
       self.categoria = categoria
       self.ativo = False
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante('Alabama', 'louco')

#restaurante_pizza = Restaurante()
# comando dir mostra os metodos atributos e construtor


print(vars(restaurante_praca))



