class Pessoa:
  # método construtor
  def __init__(self, altura, cpf) -> None:
    self.altura = altura
    self.__cpf = cpf

  def apresentar(self):
    print(f'Ola! Minha altura - {self.altura}')
    self.__coletar_documento()

  def __coletar_documento(self):
    print(f'Meu documento - {self.__cpf}')

marcos = Pessoa("1.80", "498.533.260-17")
marcos.apresentar()

# Quando há "__"(dois underlines) a função é transformada em privada, ou seja, 
# só é possível acessá-la por outra função da classe. Não é possível chamá-la de fora 
# da classe
