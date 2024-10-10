class Pessoa:

  def Altura(self, altura):
    self.altura = altura
    print(self.altura)

  def Idade(self, idade):
    self.idade = idade
    print(self.idade)

  def Correr(self, km):
    self.correr = km
    print(self.correr)

  def Comer(self, comida):
    self.comer = comida
    print(self.comer)

dados_pessoa = Pessoa()

dados_pessoa.Altura(180)
dados_pessoa.Idade(18)
dados_pessoa.Correr(15)
dados_pessoa.Comer('feijoada')