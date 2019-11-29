class Funcionario:
    def __init__(self, nome,  email, idade, documento, salario):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.documento = documento
        self.salario = salario

    def __str__(self):
        return f'Ola {self.nome}, voce foi cadastrado com secesso em nosso sistema'

    def aumentar_salario(self, valor):
        return self.salario + valor

dados_funcionario = Funcionario(
    nome= 'Guylherme',
    email= 'guylhermentr@gmail.com',
    idade= 16,
    documento= 1262385787475,
    salario= 2000.00
)


aumento = (float(input('Entre com o Valor do Aumento:'))) # Usario entrar com o valor
print(dados_funcionario)
valor= dados_funcionario.aumentar_salario(aumento) # Chama os dados do funcionario
print(valor)