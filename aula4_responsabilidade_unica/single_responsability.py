class SistemasCadastral:

  def cadastrar(self, nome: str, idade: int) -> None:
    if self.__validate_input(nome, idade):
      self.__register_user(nome, idade)
    else:
      self.__error_handle()

  def __validate_input(self, nome: str, idade: int) -> bool:
    return isinstance(nome, str) and isinstance(idade, int)
  
  def __register_user(self, nome:str, idade: int) -> None:
    print("Acessando o banco de dados...")
    print(f'Cadastrar usuario {nome}, idade {idade}')

  def __error_handle(self) -> None:
    print("Dados inválidos")

sistema = SistemasCadastral()
sistema.cadastrar("Enrico", 18)