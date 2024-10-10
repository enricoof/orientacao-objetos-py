class Mamifero:
  def __init__(self, localizacao: str) -> None:
    self.localizacao = localizacao
    self._tamanho = 1.23

  def andar(self, animal: str) -> None:
    print(f'O {animal} esta andando pelo {self.localizacao}')

  def _dormir(self, animal: str) -> None: #Metodo protegido
    print(f'O {animal} está dormindo')


class Gato(Mamifero):
  def __init__(self, localizacao: str) -> None:
    super().__init__(localizacao)

  def miar(self) -> None:
    print("O gato está miando")
    self.andar("gato")
    self._dormir("gato")
    print(self._tamanho)

cat = Gato("Uruguai")
cat.miar()
print()
cat._dormir("gato") # deveria dar erro / elementos protegidos nao sao chamados por objetos
print()
print(cat._tamanho) # elementos protegidos nao sao chamados por objetos