class Mamifero:
  def __init__(self, localizacao: str) -> None:
    self.localizacao = localizacao

  def andar(self, animal: str) -> None:
    print(f'O {animal} esta andando pelo {self.localizacao}')

class Cachorro(Mamifero):
  def __init__(self, localizacao: str) -> None:
    super().__init__(localizacao) #se refere ao contrutor da classe superior

  def latir(self) -> None:
    print("O cachorro está latindo")
    self.andar("cachorro")

class Gato(Mamifero):
  def __init__(self, localizacao: str) -> None:
    super().__init__(localizacao)

  def miar(self) -> None:
    print("O gato está miando")
    self.andar("gato")

dog = Cachorro("Chile")
dog.latir()
print()
cat = Gato("Uruguai")
cat.miar()