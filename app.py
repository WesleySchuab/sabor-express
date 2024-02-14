from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Goumert')
restaurante_mexicano = Restaurante('mexican','food')
restaurante_japones = Restaurante('japa','Japoensa')

restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()