class Carro:
    # CARRO
    def __init__(self, proprietario, modelo, cor, placa, preco, marca): # Caracteriscas dos carros
       self.proprietario = proprietario
       self.modelo = modelo
       self.cor = cor
       self.placa = placa
       self.preco = preco
       self.marca = marca

    def __str__(self):
        return f"Ola{self .proprietario}, seu carro e o {self .modelo} - {self.cor} - {self .placa} - {self .preco} - {self .marca}"
        # Retonar para o usuario as Caracteriscas
meu_carro = Carro(
    proprietario= 'Guylherme',
    modelo='Celta',
    cor= 'prata',
    placa= 'HEI 3303',
    preco= '18000',
    marca='chevrole',
    #Uma var para colocar as caracteristica
)
print(meu_carro)