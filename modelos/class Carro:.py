class Carro:
    modelo=''
    cor=''
    ano=''

class Restaurante:
    def __init__(self, nome, categoria) -> None:
        self.nome = nome
        self.categoria = categoria
        ativo = False
        
    nome=''
    categoria=''
    ativo=False
    rua=''
    bairro=''
def __str__(self) -> str:
    return f'{self.nome} {self.categoria}'

pizza = Restaurante('La_pizza','Massas')
#print(f'{pizza.nome} | {pizza.categoria} | {pizza.ativo}')
print(vars(pizza))