class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_pizza = Restaurante()
# comando dir mostra os metodos atributos e construtor
print(dir(restaurante_praca))

