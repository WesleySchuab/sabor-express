class Restaurante:
    def __init__(self, nome, categoria) -> None:
       self.nome = nome
       self.categoria = categoria
       self.ativo = False
       
    """
    O método __str__ é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto,
    mostraremos determinada informação. Podemos escolher se queremos mostrar o nome, a categoria ou o ativo. Ou seja, podemos escolher
    e definir. 
    Então, em vez de mostrar a representação do endereço de memória, ele mostrará o que decidirmos.
    """
    def __str__(self) -> str:
        return self.nome
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante('Alabama', 'louco')

#restaurante_pizza = Restaurante()
# comando dir mostra os metodos atributos e construtor


print(vars(restaurante_praca))



