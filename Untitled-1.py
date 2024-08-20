class Produto:
    def __init__(self,nome,preco):     #Método construtor
        self.nome = nome
        self.preco = preco        #self siginifica que a classe recebera a variavel do objeto


class Carrinho:

    def __init__(self):
        self.produtos =[]

    def adicionar_produto(self,produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def calcular_total(self):
        total = 0
        for p in self.produtos:
            total += p.preco

        return total
        

#declarar/instanciar objetos
produto_bone = Produto("Boné da Nike", 109.90)
produto_bermuda = Produto("Bermuda Vida marinha", 190.90)
produto_tenis = Produto("Air Jordan", 469.99)

#criar carrinho
carrinho = Carrinho()
carrinho.adicionar_produto(produto_bone)
carrinho.adicionar_produto(produto_bermuda)
carrinho.adicionar_produto(produto_tenis)

print("carrinho custa: ", carrinho.calcular_total())

carrinho.remover_produto(produto_tenis)

print("carrinho custa: ", carrinho.calcular_total())