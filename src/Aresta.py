from src.Vertice import Vertice


class Aresta:
    def __init__(self, v1: Vertice, v2: Vertice, peso: float = 1):
        self.__v1 = v1
        self.__v2 = v2
        self.__peso = peso

    def get_v1(self) -> Vertice:
        return self.__v1

    def get_v2(self) -> Vertice:
        return self.__v2

    def get_peso(self) -> float:
        return self.__peso

    def set_peso(self, peso: float) -> None:
        self.__peso = peso
