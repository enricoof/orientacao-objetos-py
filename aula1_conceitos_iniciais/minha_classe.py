class MinhaClasse:
  def __init__(self): # metodo construtor
    self.atributo_1 = "meu atributo"
    self.atributo_2 = [1, 2, "a"]

  def metodo_1(self):
    print("minha ação 1")
    print("minha ação 2")
    return "Ola mundo!"

# obejto          # classe -> instanciamos ium objeto
minha_classe = MinhaClasse()

response = minha_classe.metodo_1()
print(response)