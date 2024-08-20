class VetorNaoOrdenado:
    def __init__ (self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [''] * capacidade

    def inserir(self, valor):
        if(self.ultima_posicao == self.capacidade -1):
            print("vetor cheio")
        else:
            self.ultima_posicao +=1
            self.valores[self.ultima_posicao] = valor

    def imprimir(self):
        for i in range(self.ultima_posicao +1):
            print('Posicao {} | valor {}'.format(i, self.valores[i]))

    def pesquisar(self, valorPesquisa):
        for i in range(self.ultima_posicao +1):
            if (valorPesquisa == self.valor[i]):
                return i
            return -1
        
    def excluir(self, valorExcluir):
        pos = self.pesquisar(valorExcluir)
        if (pos == -1):
            return -1
        else:
            for i in range(pos, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao = self.ultima_posicao - 1

meuVetor = VetorNaoOrdenado(3)
meuVetor.inserir(2)
meuVetor.inserir(3)
meuVetor.inserir(4)

