class Vertice:
    def __init__(self, index: int, rotulo: str) -> None:
        self.__index = index
        self.__rotulo = rotulo
        self.__arestas = dict()

    def add_aresta(self, vizinho, peso=1) -> None:
        self.__arestas[vizinho] = peso

    def get_index(self) -> int:
        return self.__index

    def get_rotulo(self) -> str:
        return self.__rotulo

    def get_arestas(self) -> dict:
        return self.__arestas
