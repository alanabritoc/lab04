from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        return self.inicio is None

    def remove(self, item):
        if self.inicio is None:
            return

        if self.inicio.valor == item:
            self.inicio = self.inicio.get_proximo()
            return

        atual = self.inicio
        while atual.get_proximo() is not None:
            if atual.get_proximo().valor == item:
                atual.set_proximo(atual.get_proximo().get_proximo())
                return
            atual = atual.get_proximo()

    def tamanho(self) -> int:
        if self.inicio is None:
            return 0
        else:
            contador = 0
            aux = self.inicio
            while aux is not None:
                contador += 1
                aux = aux.get_proximo()
            return contador

    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        aux = self.inicio
        while aux is not None:
            if aux.valor == item:
                return True
            aux = aux.get_proximo()
        return False

    def indice_de(self, item):
        indice = 0
        atual = self.inicio
        while atual:
            if (atual.valor == item):
                return indice
            indice += 1
            atual = atual.get_proximo()
        return -1

    def recupera_indice(self, index):
        if index < 0:
            return None
        
        atual = self.inicio
        indice = 0
        
        while atual:
            if (indice == index):
                return atual.valor
            indice += 1
            atual = atual.get_proximo()
        
        return None
    
    #def remove_indice(self, indice):
        if indice < 0 or self.inicio is None:
            return None #informa que o indice é invalido ou a lista esta vazia 

        if indice == 0:
            valor= self.inicio.valor
            self.inicio=self.inicio.get_proximo()
            return valor  

        no_antes= None
        no_atual= self.inicio
        contdor= 0

        while no_atual is not None and contador < indice:
            no_antes=no_atual
            no_atual=no_atual.get_proximo()
            contador+=1

        if no_atual is None:
            return None #indice invalido

        valor=no_atual.valor
        
        if no_antes is not None:
            no_antes.set_proximo(no_atual.get_proximo())
        else:
            self.inicio= no_atual.get_proximo()
            return valor    

    
    def remove_indice(self, indice):
        if indice < 0 or self.inicio is None:
            return None

        if indice == 0:
            valor = self.inicio.valor
            self.inicio = self.inicio.get_proximo()
            return valor

        no_anterior = self.inicio
        contador = 0

        while contador < indice - 1 and no_anterior.get_proximo() is not None:
            no_anterior = no_anterior.get_proximo()
            contador += 1

        if no_anterior.get_proximo() is None:
            return None

        no_atual = no_anterior.get_proximo()
        valor = no_atual.valor
        no_anterior.set_proximo(no_atual.get_proximo())

        return valor

    class Pilha:
        def _init_(self):
            self.pilha = []

        def push(self, valor):
            self.pilha.append(valor)

        def pop(self):
            if self.esta_vazia():
                raise IndexError("A pilha está vazia")
            return self.pilha.pop()

        def tamanho(self):
            return len(self.pilha)

        def esta_vazia(self):
            return len(self.pilha) == 0    

    class Fila:
        def _init_(self):
            self.fila = []

        def enqueue(self, valor):
            self.fila.append(valor)

        def dequeue(self):
            if self.esta_vazia():
                raise IndexError("A fila está vazia")
            elemento_removido = self.fila[0]
            self.fila = self.fila[1:]
            return elemento_removido

        def tamanho(self):
            return len(self.fila)

        def esta_vazia(self):
            return len(self.fila) == 0