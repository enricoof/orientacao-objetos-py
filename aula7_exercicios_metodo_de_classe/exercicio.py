class Loja:

  taxa = 1.15

  def __init__(self, valor: float) -> None:
    self.valor_produto_bruto = valor

  def consultar_valor(self):
    valor_produto = self.valor_produto_bruto * self.taxa
    print(f'Valor do produto: {valor_produto}')

  @classmethod
  def editar_taxa(cls, valor: float):
    cls.taxa = valor

loja_praia = Loja(30.50)
loja_shopping = Loja(10.99)
loja_rua = Loja(20.45)

loja_praia.consultar_valor()
loja_shopping.consultar_valor()
loja_rua.consultar_valor()

loja_praia.editar_taxa(1.35)