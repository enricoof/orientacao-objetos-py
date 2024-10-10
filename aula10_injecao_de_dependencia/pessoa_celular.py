class Celular:
  def __init__(self, modelo: str) -> None:
    self.modelo = modelo

  def enviar_mensagem(self, mensagem: str) -> None:
    print(f'Enviando mensagem: {mensagem}')

  def abir_emails(self) -> None:
    print("Abrindo os emails...")

  def abrir_yt(self) -> None:
    print("Abrindo o youtube...")


class Pessoa:
  def __init__(self, celular: Celular) -> None:
    self.__celular = celular

  def pedir_pizza(self) -> None:
    print("Buscando celular...")
    print("Definindo sabor...")
    self.__celular.enviar_mensagem("Quero uma pizza de calabresa")
    print("Agurdando chegada")

  def estudar(self) -> None:
    print("Abrindo o computador")
    self.__celular.abrir_yt()
    print("Anotando o conteúdo")

iphone = Celular("Iphone")
android = Celular("Android")

agnaldo = Pessoa(android)
tomas = Pessoa(iphone)

agnaldo.estudar()
print()
tomas.pedir_pizza()