class Programa:
    def __init__(self, nome, ano):
        self.__nome =nome.title()
        self.ano = ano
        self._likes = 0