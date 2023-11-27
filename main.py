class Programa:
    def __init__(self, nome, ano):
        self.__nome =nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self.__likes +=1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)
